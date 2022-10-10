import argparse
import enum
import sys
from typing import Optional

from .__version__ import __version__
from .loader import EmptyGifLoaderError, GifLoader

if sys.version_info >= (3, 9):
    from importlib.resources import files
else:
    from importlib_resources import files


@enum.unique
class StringOutputFormat(str, enum.Enum):
    HTML = "HTML"
    MARKDOWN = "Markdown"


def gif_to_string_output(
    gif: dict,
    output_format: StringOutputFormat,
    desired_width: Optional[int] = None,
    lazy: bool = False,
) -> str:
    """Converts a gif object to a particular string format.

    Args:
        gif:
            Image data containing at least `name` and `url`.
        output_format:
            Currently only HTML and Markdown are supported.
        desired_width:
            Desired width of the rendered image. Only supported in HTML mode.
            If not specified (i.e., None), then the img's original width is used.
            The height will be automatically calculated based on the desired width.
        lazy:
            Whether to use lazy or eager loading. Only supported in HTML mode.
            Defaults to False.

    Returns:
        A string representation of the image, in the specified format.

    """
    name = gif["name"]
    url = gif["url"]

    if output_format == StringOutputFormat.HTML:
        # NOTE: It is recommended to always set the width and height attributes on the img
        # so that the browser knows how much space to allocate the image.
        width = gif["width"]
        height = gif["height"]
        if desired_width:
            aspect_ratio = width / height
            width = desired_width
            height = int(width / aspect_ratio)

        t_alt = f' alt="{name}"'
        t_src = f' src="{url}"'
        t_width = f' width="{width}"'
        t_height = f' height="{height}"'
        t_loading = ' loading="lazy"' if lazy else ""
        t = f"<img{t_loading}{t_alt}{t_src}{t_width}{t_height}>"
        return t
    if output_format == StringOutputFormat.MARKDOWN:
        if desired_width is not None:
            raise ValueError("desired_width is not supported when output_format is Markdown")
        return f"![{name}]({url})"
    raise ValueError(f"output_format: {output_format!r} not supported.")


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Get a randomly-generated LGTM gif or image.",
    )
    parser.add_argument(
        "-V",
        "--version",
        action="version",
        version=f"%(prog)s {__version__}",
    )
    parser.add_argument(
        "-I",
        "--include",
        action="append",
        help=(
            "Apply an inclusive filter on the list of gifs before random choice (matches are included). "
            "The filter condition is treated as a regex query if it starts with ^ and ends with $. "
            "For non-regex conditions, a simple substring check is used. Multiple conditions are supported. "
            "Exclusions are given higher priority over inclusions."
        ),
        metavar="PATTERN",
    )
    parser.add_argument(
        "-E",
        "--exclude",
        action="append",
        help=(
            "Apply an exclusive filter on the list of gifs before random choice (matches are excluded). "
            "The filter condition is treated as a regex query if it starts with ^ and ends with $. "
            "For non-regex conditions, a simple substring check is used. Multiple conditions are supported. "
            "Exclusions are given higher priority over inclusions."
        ),
        metavar="PATTERN",
    )
    parser.add_argument(
        "-wd",
        "--width",
        help=(
            "Specify the width of the output gif. A non-positive width will result in an error. "
            "Only applicable for HTML."
        ),
        type=int,
    )
    args = parser.parse_args()

    resource_path = files("lgtm_db") / "data/db.yaml"
    gloader = GifLoader.from_yaml(resource_path)

    if args.include:
        for ft in args.include:
            gloader.filter_by_name(ft, complement=False)
    if args.exclude:
        for ft in args.exclude:
            gloader.filter_by_name(ft, complement=True)

    try:
        chosen = gloader.pick_random()
    except EmptyGifLoaderError as e:
        print(str(e), file=sys.stderr)
        return 1

    # config output gif
    if args.width is not None and args.width <= 0:
        print("[ERR] Specified width must be non-negative.", file=sys.stderr)
        return 1

    output = gif_to_string_output(
        chosen,
        output_format=StringOutputFormat.HTML,
        desired_width=args.width,
        lazy=False,
    )
    print(output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
