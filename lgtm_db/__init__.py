import enum
import random
import sys
from typing import Optional

import yaml

try:
    from yaml.cyaml import CSafeLoader as Loader
except ImportError:
    from yaml import SafeLoader as Loader

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
            Defaults to 500.
        lazy:
            Whether to use lazy or eager loading. Only supported in HTML mode.
            Defaults to False.

    Returns:
        A string representation of the image, in the specified format.
    """
    name = gif["name"]
    url = gif["url"]

    if output_format == StringOutputFormat.HTML:
        aspect_ratio = gif["width"] / gif["height"]
        width = desired_width or 500  # TODO: add logic for gif["width"]
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
    resource_path = files("lgtm_db") / "data/db.yaml"
    with resource_path.open(mode="r") as f:
        contents = yaml.load(f, Loader=Loader)

    all_lgtm = contents["images"] + contents["gifs"]
    chosen = random.choice(all_lgtm)

    output = gif_to_string_output(
        chosen,
        output_format=StringOutputFormat.HTML,
        desired_width=500,
    )
    print(output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
