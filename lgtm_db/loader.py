import itertools as it
import random

import yaml

try:
    from yaml.cyaml import CSafeLoader as YamlLoader
except ImportError:
    from yaml import SafeLoader as YamlLoader


class EmptyGifLoaderError(Exception):
    pass


class GifLoader:
    """A generic container for holding Gifs."""

    def __init__(self, gifs):
        """TBD: type hinting for gifs

        gifs should be a list of Gif dictionaries, consisting of name, url, ...
        """
        self.gifs = gifs
        self._mask = [True for _ in self.gifs]

    def filter_by_name(self, name: str):
        self._mask = [m and name in g["name"] for m, g in zip(self._mask, self.gifs)]
        return self

    def pick_random(self):
        if not all(self._mask):
            # worst case scenario: this duplicates the entire list, doubling memory usage.
            # thus, we only enter this branch if some filters have been successfully applied.
            candidates = list(it.compress(self.gifs, self._mask))
        else:
            candidates = self.gifs

        if not candidates:
            raise EmptyGifLoaderError

        return random.choice(candidates)

    @classmethod
    def from_db(cls, filepath):
        with filepath.open(mode="r") as f:
            contents = yaml.load(f, Loader=YamlLoader)

        # FIXME: this isn't elegant, I should make this more generic somehow.
        return cls(contents["images"] + contents["gifs"])
