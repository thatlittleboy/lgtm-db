"""Temporary script to append on width and height attributes to db.yaml

Needs cleaning up... And move to using async, etc.
"""
import argparse
import asyncio
from io import BytesIO
from pathlib import Path
from typing import Any

import aiohttp
import yaml
from PIL import Image

try:
    from yaml.cyaml import CSafeLoader as Loader
except ImportError:
    from yaml import SafeLoader as Loader


async def _gather_with_concurrency(tasks, n):
    """Helper function for limiting async concurrency."""
    semaphore = asyncio.Semaphore(n)

    async def sem_wrapper(task):
        async with semaphore:
            return await task

    return await asyncio.gather(*(sem_wrapper(task) for task in tasks))


async def get_size_from_url(url) -> tuple[int, int]:
    print(f"Getting image size from {url!r}")
    timeout = aiohttp.ClientTimeout(total=20)
    async with aiohttp.ClientSession(timeout=timeout) as session:
        image_raw = await session.get(url, raise_for_status=True)
        bytez = await image_raw.read()
    image = Image.open(BytesIO(bytez))
    return image.size


async def main() -> int:
    project_path = Path(__file__).parent.parent

    # load data contents
    db_path = project_path / "lgtm_db/data/db.yaml"
    with db_path.open(mode="r") as f:
        contents = yaml.load(f, Loader=Loader)

    data: list[dict[str, Any]] = contents["images"] + contents["gifs"]

    # obtain image width/height from url
    sizes: list[tuple[int, int]] = await _gather_with_concurrency(
        [get_size_from_url(p["url"]) for p in data],
        n=10,
    )

    # replace the image size data back into the db
    for p, size in zip(data, sizes, strict=True):
        p["width"], p["height"] = size

    new_db_path = db_path.parent / "new_db.yaml"
    with new_db_path.open(mode="w") as f:
        yaml.safe_dump(data, f, sort_keys=False)

    return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--query",
        help="query the image size from a single url",
        type=str,
        default=None,
    )
    args = parser.parse_args()

    if args.query:
        task = get_size_from_url(args.query)
        print(asyncio.run(task))
        raise SystemExit(0)

    raise SystemExit(asyncio.run(main()))
