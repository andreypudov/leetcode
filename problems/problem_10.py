# 10. Regular Expression Matching
#
# Given an input string s and a pattern p, implement regular expression matching
# with support for '.' and '*' where:
#
# - '.' Matches any single character.​​​​
# - '*' Matches zero or more of the preceding element.
#
# The matching should cover the entire input string (not partial).
#
# Constraints:
#
# - 1 <= s.length <= 20
# - 1 <= p.length <= 20
# - s contains only lowercase English letters.
# - p contains only lowercase English letters, '.', and '*'.
# - It is guaranteed for each appearance of the character '*', there will be a
#   previous valid character to match.


class Token:
    def __init__(self, value: str, isStar: bool):
        self.value = value
        self.isStar = isStar

    def __hash__(self):
        return hash((self.value, self.isStar))

    def __eq__(self, other):
        return self.value == other.value and self.isStar == other.isStar

    def __str__(self):
        return f"Token({self.value}, {self.isStar})"

    def __repr__(self):
        return self.__str__()


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        tokens = self.tokenize(p)
        tokens = self.removeDuplicateTokens(tokens)

        return self.shift(s, tokens)

    def shift(self, string: str, pattern: list[Token]) -> bool:
        if len(string) == 0 and len(pattern) == 0:
            return True
        if len(string) == 0 and self.nonstarlen(pattern) == 0:
            return True
        elif len(string) == 0 and len(pattern) != 0:
            return False
        elif len(string) != 0 and len(pattern) == 0:
            return False

        token = pattern[0]
        char = string[0]

        if token.isStar:
            if self.match(char, token):
                return self.shift(string[1:], pattern) or self.shift(
                    string, pattern[1:]
                )
            else:
                return self.shift(string, pattern[1:])
        else:
            if self.match(char, token):
                return self.shift(string[1:], pattern[1:])
            else:
                return False

        return False

    def removeDuplicateTokens(self, tokens: list[Token]) -> list[Token]:
        result = []
        previous = tokens[0]

        result.append(previous)

        for index in range(1, len(tokens)):
            token = tokens[index]
            if previous.isStar == token.isStar is True and (
                previous.value == token.value or previous.value == "."
            ):
                continue

            previous = token
            result.append(token)

        return result

    def match(self, char: str, token: Token) -> bool:
        return True if char == token.value or token.value == "." else False

    def nonstarlen(self, tokens: list[Token]) -> int:
        count = 0
        for token in tokens:
            if not token.isStar:
                count += 1
        return count

    def tokenize(self, pattern: str) -> list[Token]:
        tokens = []

        for i in range(len(pattern)):
            if pattern[i] == "*":
                tokens[-1].isStar = True
            else:
                tokens.append(Token(pattern[i], False))

        return tokens
