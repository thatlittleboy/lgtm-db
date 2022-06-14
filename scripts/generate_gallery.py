from pathlib import Path

import yaml
from bs4 import BeautifulSoup
from bs4.dammit import EntitySubstitution
from bs4.formatter import HTMLFormatter

try:
    from yaml.cyaml import CSafeLoader as Loader
except ImportError:
    from yaml import SafeLoader as Loader

from lgtm_db import StringOutputFormat, gif_to_string_output


class GalleryFormatter(HTMLFormatter):
    def __init__(self):
        # html5: https://bazaar.launchpad.net/~leonardr/beautifulsoup/bs4/view/head:/bs4/formatter.py#L166
        super().__init__(
            entity_substitution=EntitySubstitution.substitute_html,
            void_element_close_prefix=None,
            empty_attributes_are_booleans=True,
            indent=2,
        )

    def attributes(self, tag):
        if tag.attrs is None:
            return None
        for k, v in tag.attrs.items():
            if k == "m":
                continue
            yield k, v


def render_section(resources: list, section_title: str) -> str:
    """Renders a particular section given a section title in HTML format."""
    body = f"<h2>{section_title.title()}</h2>\n"
    section_contents = []

    # For some reason, turning on lazy loading for the first 5 (say), and eager for the
    #   remainder makes the lazy-loading not work properly.. No idea why that is the
    #   case.
    for idx, rsrc in enumerate(resources):
        name = rsrc["name"]
        img_tag = gif_to_string_output(
            rsrc,
            output_format=StringOutputFormat.HTML,
            desired_width=420,
            lazy=idx >= 0,
        )
        section_contents.append(rf"<b>Name</b>: {name}<br>{img_tag}")

    body += "\n\n".join(section_contents)
    return body


def write_html_file(path: Path, contents: str) -> None:
    """Writes the string contents to the file path"""
    if path.exists():
        print(" Overwriting! ")

    path.write_text(contents)


def main() -> int:
    # NOTE: doing this method instead of importlib.resources to extract the paths
    #   because this script is meant to be run even without installing the package.
    #   the disadvantage here is that this script will be less portable.
    project_path = Path(__file__).parent.parent

    template_path = project_path / "docs/assets/template-index.html"
    soup = BeautifulSoup(template_path.read_text(), "html.parser")

    # load data
    db_path = project_path / "lgtm_db/data/db.yaml"
    with db_path.open(mode="r") as f:
        contents = yaml.load(f, Loader=Loader)

    # generate HTML body
    data = []
    for section_title, resources in contents.items():
        data.append(render_section(resources, section_title))

    body = BeautifulSoup("\n\n".join(data), "html.parser")
    soup.find("body").string.replace_with(body)

    # write out final html
    write_path = project_path / "docs/index.html"
    write_html_file(
        path=write_path,
        contents=soup.prettify(formatter=GalleryFormatter()),
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
