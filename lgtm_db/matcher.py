import re


class Matcher:
    def __init__(self, condition: str):
        self.condition = condition
        self.regexed: bool = self.is_regex_pattern(condition)

        # precompile the regex pattern, if needed
        if self.regexed:
            self._pattern = re.compile(condition)

    @staticmethod
    def is_regex_pattern(s: str) -> bool:
        """Checks if a string is an accepted regex pattern.

        A string is only regarded as a regex pattern if it starts with "^" and ends with "$".

        Example:

            >>> Matcher.is_regex_pattern(r"^good.+$")
            True
            >>> Matcher.is_regex_pattern(r"lgtm_gif")
            False

        """
        return s.startswith(r"^") and s.endswith(r"$")

    def match(self, name: str) -> bool:
        """Checks if the given string matches the given `Matcher` condition.

        Example:

            >>> Matcher("good").match("good-boy")
            True
            >>> Matcher("bad").match("good-boy")
            False
            >>> Matcher(r"^good.+$").match("good-boy")
            True
            >>> Matcher(r"^good$").match("good-boy")
            False

        """
        if self.regexed:
            return bool(self._pattern.match(name))
        else:
            return self.condition in name
