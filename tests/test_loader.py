import pytest

from lgtm_db.loader import EmptyGifLoaderError, GifLoader


def test_load_from_yaml(sample_yaml_filepath):
    gloader = GifLoader.from_yaml(sample_yaml_filepath)

    # check gifs are loaded properly
    assert len(gloader.gifs) == 2
    expected_keys = {"name", "url", "width", "height"}
    assert not gloader.gifs[0].keys() ^ expected_keys


def test_load_from_gifs(sample_gifs):
    gloader = GifLoader(sample_gifs)

    # check gifs are loaded properly
    assert len(gloader.gifs) == 2
    expected_keys = {"name", "url", "width", "height"}
    assert not gloader.gifs[0].keys() ^ expected_keys


def test_error_when_picking_empty_initial():
    """Should raise error if gifs is empty at time of picking."""
    gloader = GifLoader([])

    with pytest.raises(EmptyGifLoaderError, match="No valid gifs"):
        gloader.pick_random()


def test_error_when_picking_empty_after_masking(sample_gifs):
    """Should raise error if gifs is empty at time of picking."""
    gloader = GifLoader(sample_gifs)
    gloader.filter_by_name(name="aghast")

    with pytest.raises(EmptyGifLoaderError, match="No valid gifs"):
        gloader.pick_random()
