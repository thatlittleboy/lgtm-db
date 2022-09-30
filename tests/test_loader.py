import pytest

from lgtm_db.loader import EmptyGifLoaderError, GifLoader


def test_load_from_yaml(sample_yaml_filepath):
    gloader = GifLoader.from_yaml(sample_yaml_filepath)

    # check gifs are loaded properly
    assert len(gloader.gifs) == 3
    expected_keys = {"name", "url", "width", "height"}
    assert not gloader.gifs[0].keys() ^ expected_keys


def test_load_from_gifs(sample_gifs):
    gloader = GifLoader(sample_gifs)

    # check gifs are loaded properly
    assert len(gloader.gifs) == 3
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


def test_single_filter_by_name_inclusive(sample_gifs):
    candidates = GifLoader(sample_gifs).filter_by_name(name="doge-thum")._get_candidates()

    assert len(candidates) == 1
    assert candidates[0]["name"] == "doge-thumbsup"


def test_single_filter_by_name_exclusive(sample_gifs):
    candidates = GifLoader(sample_gifs).filter_by_name(name="doge", complement=True)._get_candidates()

    assert len(candidates) == 1
    assert candidates[0]["name"] == "cat-thumbsup"


def test_multiple_filter_by_name_inc(sample_gifs):
    # inclusive-only
    candidates = (
        GifLoader(sample_gifs).filter_by_name(name="doge-thum").filter_by_name(name="cat")._get_candidates()
    )

    assert len(candidates) == 2
    expected_names = {
        "doge-thumbsup",
        "cat-thumbsup",
    }
    actual_names = {c["name"] for c in candidates}
    assert not expected_names ^ actual_names


def test_multiple_filter_by_name_exc(sample_gifs):
    # exclusive-only
    candidates = (
        GifLoader(sample_gifs)
        .filter_by_name(name="doge-thum", complement=True)
        .filter_by_name(name="cat", complement=True)
        ._get_candidates()
    )

    assert len(candidates) == 1
    expected_names = {
        "doge-crying",
    }
    actual_names = {c["name"] for c in candidates}
    assert not expected_names ^ actual_names


def test_multiple_filter_by_name_mixed1(sample_gifs):
    """When applying multiple filters, order matters!

    Exclusions are given higher priority than inclusions, which means we run the inclusion masking first,
    before running the exclusion masking.

    """
    # inclusive, then exclusive
    candidates = (
        GifLoader(sample_gifs)
        .filter_by_name(name="thumbsup", complement=False)
        .filter_by_name(name="doge", complement=True)
        ._get_candidates()
    )

    assert len(candidates) == 1
    expected_names = {
        "cat-thumbsup",
    }
    actual_names = {c["name"] for c in candidates}
    assert not expected_names ^ actual_names
