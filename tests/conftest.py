from pathlib import Path
from textwrap import dedent

import pytest


@pytest.fixture(scope="package")
def sample_gifs():
    gifs = [
        {
            "name": "doge-thumbsup",
            "url": "https://xyz.com/doge",
            "width": 350,
            "height": 400,
        },
        {
            "name": "doge-crying",
            "url": "https://xyz.com/doge",
            "width": 850,
            "height": 300,
        },
        {
            "name": "cat-thumbsup",
            "url": "https://xyz.com/cat",
            "width": 380,
            "height": 350,
        },
    ]
    return gifs


@pytest.fixture(scope="package")
def sample_yaml_filepath():
    filepath = Path("sample_db.yaml")

    gifs = dedent(
        """\
        images: []
        gifs:
          - name: doge-thumbsup
            url: https://xyz.com/doge
            width: 350
            height: 400
          - name: doge-crying
            url: https://xyz.com/doge
            width: 850
            height: 300
          - name: cat-thumbsup
            url: https://xyz.com/cat
            width: 380
            height: 350
        """,
    )
    filepath.write_text(gifs)
    yield filepath
    filepath.unlink()
