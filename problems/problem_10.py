# Given an input string s and a pattern p, implement regular expression matching
# with support for '.' and '*' where:
#
# - '.' Matches any single character.​​​​
# - '*' Matches zero or more of the preceding element.
#
# The matching should cover the entire input string (not partial).

# Algorithm:
# If token is not star:
#   if token matches char, then shift both string and pattern
#   else return False
# If token is star:
#   if token matches char, then shift string and keep pattern
#   else shift pattern and keep string


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
        tokens = self.tokenize(p)
        tokens = self.__remove_duplicate_tokens(tokens)

        return self.__shift(s, tokens)

    def __shift(self, string: str, pattern: list[Token]) -> bool:
        if len(string) == 0 and len(pattern) == 0:
            return True
        if len(string) == 0 and self.__non_star_len(pattern) == 0:
            return True
        elif len(string) == 0 and len(pattern) != 0:
            return False
        elif len(string) != 0 and len(pattern) == 0:
            return False

        token = pattern[0]
        char = string[0]

        if token.is_star:
            if self.__match(char, token):
                return self.__shift(string[1:], pattern) or self.__shift(
                    string, pattern[1:]
                )
            else:
                return self.__shift(string, pattern[1:])
        else:
            if self.__match(char, token):
                return self.__shift(string[1:], pattern[1:])
            else:
                return False

        return False

    def __remove_duplicate_tokens(self, tokens: list[Token]) -> list[Token]:
        result = []
        previous = tokens[0]

        result.append(previous)

        for index in range(1, len(tokens)):
            token = tokens[index]
            if (
                previous.is_star
                and token.is_star
                and (previous.value == token.value or previous.value == ".")
            ):
                continue

            previous = token
            result.append(token)

        return result

    def __match(self, char: str, token: Token) -> bool:
        return True if char == token.value or token.value == "." else False

    def __non_star_len(self, tokens: list[Token]) -> int:
        count = 0
        for token in tokens:
            if not token.is_star:
                count += 1
        return count

    def tokenize(self, pattern: str) -> list[Token]:
        tokens = []

        for _, token in enumerate(pattern):
            if token == "*":
                tokens[-1].is_star = True
            else:
                tokens.append(Token(token, False))

        return tokens
