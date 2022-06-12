import enum
import random
import sys
from typing import Optional

import yaml

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
) -> str:
    name = gif["name"]
    url = gif["url"]
    aspect_ratio = gif["width"] / gif["height"]

    if output_format == StringOutputFormat.HTML:
        width = desired_width or 500  # TODO: add logic for gif["width"]
        height = width / aspect_ratio
        return f'<img alt="{name}" src="{url}" width="{width}" height="{height}">'
    if output_format == StringOutputFormat.MARKDOWN:
        if desired_width is not None:
            raise ValueError("desired_width is not supported when output_format is Markdown")
        return f"![{name}]({url})"
    raise ValueError(f"output_format: {output_format!r} not supported.")


def main() -> int:
    resource_path = files("lgtm_db") / "data" / "db.yaml"
    with resource_path.open(mode="r") as f:
        ps = yaml.safe_load(f)

    all_lgtm = ps["images"] + ps["gifs"]
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
