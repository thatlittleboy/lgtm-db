"""Temporary script to append on width and height attributes to db.yaml

Needs cleaning up... And move to using async, etc.
"""
from io import BytesIO
from pathlib import Path

import requests
import yaml
from PIL import Image


def get_size(url):
    image_raw = requests.get(url)
    image = Image.open(BytesIO(image_raw.content))
    return image.size


project_path = Path(__file__).parent.parent

db_path = project_path / "lgtm_db" / "data" / "db.yaml"
with db_path.open(mode="r") as f:
    ps = yaml.safe_load(f)

all_contents = ps["images"] + ps["gifs"]
for p in all_contents:
    sze = get_size(p["url"])
    p["width"] = sze[0]
    p["height"] = sze[1]
    print(p["name"])

new_db_path = db_path.parent / "new_db.yaml"
with new_db_path.open(mode="w") as f:
    yaml.safe_dump(ps, f, sort_keys=False)