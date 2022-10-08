import pytest

from lgtm_db.matcher import Matcher


def test_matcher_type():
    # regex
    assert Matcher.is_regex_pattern("^$")
    assert Matcher.is_regex_pattern(r"^good.+$")

    # string
    assert not Matcher.is_regex_pattern("")
    assert not Matcher.is_regex_pattern(r"lgtm_gif")
    assert not Matcher.is_regex_pattern(r"$hahah$")


def test_condition_is_wrong_type():
    with pytest.raises(TypeError, match="expected a str, got"):
        _ = Matcher(None)
        _ = Matcher(123)
        _ = Matcher(["a", "b", "c"])
        _ = Matcher({"xyz"})


def test_match_for_regex():
    assert Matcher(r"^good.+$").match("good-boy")
    assert Matcher(r"^good.boy$").match("good-boy")
    assert not Matcher(r"^good$").match("good-boy")


def test_match_for_string():
    """When matching on string, should be a "substring" logic."""
    assert Matcher("good").match("good-boy")
    assert not Matcher("bad").match("good-boy")
    assert not Matcher("good.boy").match("good-boy")
