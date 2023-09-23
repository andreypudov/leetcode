# Given an input string s and a pattern p, implement regular expression matching
# with support for '.' and '*' where:
#
# - '.' Matches any single character.​​​​
# - '*' Matches zero or more of the preceding element.
#
# The matching should cover the entire input string (not partial).


class Token:
    def __init__(self, value: str, is_star: bool):
        self.value = value
        self.is_star = is_star

    def __hash__(self):
        return hash((self.value, self.is_star))

    def __eq__(self, other):
        return self.value == other.value and self.is_star == other.is_star

    def __str__(self):
        return f"Token({self.value}, {self.is_star})"

    def __repr__(self):
        return self.__str__()


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        pass

    def tokenize(self, pattern: str) -> list[Token]:
        tokens = []

        for i in range(len(pattern)):
            if pattern[i] == "*":
                tokens[-1].is_star = True
            else:
                tokens.append(Token(pattern[i], False))

        return tokens
