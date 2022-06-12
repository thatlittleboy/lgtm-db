from pathlib import Path

import yaml

from lgtm_db import StringOutputFormat, gif_to_string_output


def render_section(resources: list, section_title: str) -> str:
    """Renders a particular section given a section title in markdown format.

    Loads the first 5 images eagerly and the remaining lazily, for efficiency
    reasons.
    """
    body = f"<h2>{section_title.title()}</h2>\n"
    section_contents = []

    for idx, rsrc in enumerate(resources):
        name = rsrc["name"]
        img_tag = gif_to_string_output(
            rsrc,
            output_format=StringOutputFormat.HTML,
            desired_width=420,
            lazy=idx >= 5,
        )
        section_contents.append(rf"<strong>Name</strong>: {name}<br>{img_tag}")

    body += "\n".join(section_contents)
    return body


def write_md_file(path: Path, contents: str) -> None:
    """Writes the string contents to the file path"""
    if path.exists():
        print(" Overwriting! ")

    path.write_text(contents)


def main() -> int:
    # NOTE: doing this method instead of importlib.resources to extract the paths
    #   because this script is meant to be run even without installing the package.
    #   the disadvantage here is that this script will be less portable.
    project_path = Path(__file__).parent.parent

    db_path = project_path / "lgtm_db" / "data" / "db.yaml"
    with db_path.open(mode="r") as f:
        ps = yaml.safe_load(f)

    all_contents = []
    for section_title, resources in ps.items():
        all_contents.append(render_section(resources, section_title))

    write_path = project_path / "docs" / "gallery.md"
    write_md_file(
        path=write_path,
        # add a new line at end-of-file to stop pre-commit from complaining
        contents="\n\n".join(all_contents) + "\n",
    )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
