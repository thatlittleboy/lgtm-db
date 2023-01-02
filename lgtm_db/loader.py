import itertools as it
import random

import yaml

try:
    from yaml.cyaml import CSafeLoader as YamlLoader
except ImportError:
    from yaml import SafeLoader as YamlLoader

from lgtm_db.matcher import Matcher


class EmptyGifLoaderError(Exception):
    pass


class GifLoader:
    """A generic container for holding Gifs."""

    def __init__(self, gifs):
        self.gifs = gifs
        self._mask = [None for _ in self.gifs]

    def filter_by_name(self, name: str, complement: bool = False):
        """Applies a mask on the candidate gifs based on its name."""
        matcher = Matcher(name)
        if complement:
            # logic for exclusions (higher priority than inclusions):
            # m == False: should always return False
            # m == None/True: should return `not match`
            self._mask = [not (m is False or matcher.match(g["name"])) for m, g in zip(self._mask, self.gifs)]
        else:
            # logic for inclusions:
            # m == True: should always return True
            # m == None/False: should return `match`
            self._mask = [m or matcher.match(g["name"]) for m, g in zip(self._mask, self.gifs)]
        return self

    def pick_random(self):
        """Returns a randomly chosen gif after applying the specified filters."""
        candidates = self._get_candidates()
        # print([c["name"] for c in candidates])

        if not candidates:
            emsg = "[ERR] No valid gifs were found!"
            raise EmptyGifLoaderError(emsg)
        return random.choice(candidates)

    def _get_candidates(self):
        """Returns the list of candidate gifs after applying the specified filters."""
        if any(m is False for m in self._mask):
            # worst case scenario: this duplicates the entire list, doubling memory usage.
            # thus, we only enter this branch if some filters have been successfully applied.
            candidates = list(it.compress(self.gifs, self._mask))
        else:
            candidates = self.gifs
        return candidates

    @classmethod
    def from_yaml(cls, filepath):
        with filepath.open(mode="r") as f:
            contents = yaml.load(f, Loader=YamlLoader)

        # FIXME: this isn't elegant, I should make this more generic somehow.
        return cls(contents["images"] + contents["gifs"])
