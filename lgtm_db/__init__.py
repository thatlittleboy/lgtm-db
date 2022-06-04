import random
from pathlib import Path

import yaml


def main() -> int:
    p = Path("lgtm.yaml")
    with p.open(mode="r") as f:
        ps = yaml.safe_load(f)

    all_lgtm = ps["images"] + ps["gifs"]
    chosen = random.choice(all_lgtm)

    print(
        '<img alt="{name}" src="{url}" width="500">'.format(**chosen),
    )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
