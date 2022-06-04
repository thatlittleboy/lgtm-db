import random
import sys

import yaml

if sys.version_info >= (3, 9):
    from importlib.resources import files
else:
    from importlib_resources import files


def main() -> int:
    resource_path = files("lgtm_db") / "data" / "db.yaml"
    with resource_path.open(mode="r") as f:
        ps = yaml.safe_load(f)

    all_lgtm = ps["images"] + ps["gifs"]
    chosen = random.choice(all_lgtm)

    print(
        '<img alt="{name}" src="{url}" width="500">'.format(**chosen),
    )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
