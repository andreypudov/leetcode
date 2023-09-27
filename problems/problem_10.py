# Given an input string s and a pattern p, implement regular expression matching
# with support for '.' and '*' where:
#
# - '.' Matches any single character.​​​​
# - '*' Matches zero or more of the preceding element.
#
# The matching should cover the entire input string (not partial).


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
    step: int = 1
    str_len: int = 0
    ptrn_len: int = 0

    def isMatch(self, s: str, p: str) -> bool:
        tokens = self.tokenize(p)
        self.str_len = len(s)
        self.ptrn_len = len(tokens)

        # print(f"\nstring: {s}")
        # print(f"tokens: {self.toStr(tokens)}")

        tokens = self.shiftNotMatched(s, tokens)
        result = self.shift(s, tokens)
        print(f"result: {result}")
        return result

    def shiftNotMatched(self, string: str, pattern: list[Token]) -> list[Token]:
        for index, token in enumerate(pattern):
            if self.isMatchToken(string[0], token):
                return pattern[index:]
        return []

    def shift(self, string: str, pattern: list[Token]) -> bool:
        if len(string) == 0 or len(pattern) == 0:
            # print(f"{self.step} End of string or pattern | {string} {pattern}")
            return False

        char = string[0]
        token = pattern[0]
        patternCompleted = self.isPatternCompleted(pattern[1:])
        print(
            f"{self.step} BEGIN {char} => {token.value} | {self.str_len - len(string)} {self.ptrn_len - len(pattern)}"
        )

        if (
            self.isMatchToken(char, token) and len(string) == 1 and patternCompleted
        ):  # len(pattern) == 1
            # print(f"{self.step} MATCHED {char} == {token.value}")
            return True

        if not self.isMatchToken(char, token):
            if token.isStar and not patternCompleted:
                return self.shift(string, pattern[1:])
            else:
                print(f"{self.step} END {char} != {token.value}")
                self.step += 1
                return False

        if token.isStar:
            for index, char in enumerate(string):
                # print(f"{self.step} -- NEXT in {string} | {index} {char} {token.value}")
                if self.isMatchToken(char, token):
                    if len(string) - index == 1 and patternCompleted:
                        # print(f"{self.step} MATCHED 3")
                        return True
                    if len(pattern) == 1:
                        # print("END OF PATTERN")
                        # self.step += 1
                        continue
                    new_pattern = pattern
                    new_pattern[0].isStar = False
                    result = self.shift(string[index:], new_pattern)
                    if result:
                        # print(f"{self.step} MATCHED 4")
                        return result
                else:
                    return False

            # print(f"{self.step} NOT MATCHED")
            # self.step += 1
            return False
        else:
            return self.shift(string[1:], pattern[1:])

    def isMatchToken(self, char: str, token: Token) -> bool:
        return token.value == char or token.value == "."

    def isPatternCompleted(self, pattern: list[Token]) -> bool:
        requiredTokens = 0

        for token in pattern:
            if not token.isStar:
                requiredTokens += 1

        return requiredTokens == 0

    def tokenize(self, pattern: str) -> list[Token]:
        tokens = []

        for i in range(len(pattern)):
            if pattern[i] == "*":
                tokens[-1].isStar = True
            else:
                tokens.append(Token(pattern[i], False))

        return tokens

    def toStr(self, tokens: list[Token]) -> str:
        result = ""
        for token in tokens:
            result += f"{token.value + '*' if token.isStar else token.value}"
        return result


s = Solution()
# s.isMatch("a", "ab*")
# s.isMatch("aa", "a*")
# s.isMatch("ab", ".*c")
# s.isMatch("aaa", "ab*ac*a")
# s.isMatch("aab", "c*a*b")
# s.isMatch("mississippi", "mis*is*p.")
s.isMatch("ba", ".*a*a")
# s.isMatch("bbbba", ".*a*a")
