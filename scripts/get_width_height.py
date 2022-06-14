"""Temporary script to append on width and height attributes to db.yaml

Needs cleaning up... And move to using async, etc.
"""
from io import BytesIO
from pathlib import Path

import requests
import yaml
from PIL import Image

try:
    from yaml.cyaml import CSafeLoader as Loader
except ImportError:
    from yaml import SafeLoader as Loader


def get_size(url):
    image_raw = requests.get(url)
    image = Image.open(BytesIO(image_raw.content))
    return image.size


def main() -> int:
    project_path = Path(__file__).parent.parent

    db_path = project_path / "lgtm_db/data/db.yaml"
    with db_path.open(mode="r") as f:
        contents = yaml.load(f, Loader=Loader)

    data = contents["images"] + contents["gifs"]
    for p in data:
        print(p["name"])
        p["width"], p["height"] = get_size(p["url"])

    new_db_path = db_path.parent / "new_db.yaml"
    with new_db_path.open(mode="w") as f:
        yaml.safe_dump(data, f, sort_keys=False)


if __name__ == "__main__":
    raise SystemExit(main())
