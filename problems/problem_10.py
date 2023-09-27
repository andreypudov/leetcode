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
    step: int = 1
    str_len: int = 0
    ptrn_len: int = 0

    def isMatch(self, s: str, p: str) -> bool:
        tokens = self.tokenize(p)
        self.str_len = len(s)
        self.ptrn_len = len(tokens)

        print(f"\nstring: {s}")
        print(f"tokens: {self.toStr(tokens)}")

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
            print(f"{self.step} End of string or pattern | {string} {pattern}")
            return False

        # self.step += 1
        # print(f'\n{self.step} BEGIN {string}:{len(string)} {self.toStr(pattern)}:{len(pattern)}')

        char = string[0]
        token = pattern[0]
        print(
            f"{self.step} BEGIN {char} => {token.value} | {self.str_len - len(string)} {self.ptrn_len - len(pattern)}"
        )

        if self.isMatchToken(char, token) and len(string) == 1 and len(pattern) == 1:
            print(f"{self.step} MATCHED {char} == {token.value}")
            return True

        if not self.isMatchToken(char, token):
            if token.is_star and len(pattern) > 1:
                return self.shift(string, pattern[1:])
            else:
                # or len(string) == 1 or len(pattern) == 1:
                # print(f'{self.step} END {self.isMatchToken(char, token)} | {self.str_len - len(string)} {self.ptrn_len - len(pattern)}')
                # self.step += 1
                print(f"{self.step} END {char} != {token.value}")
                self.step += 1
                return False

        if token.is_star:
            for index, char in enumerate(string):
                print(f"{self.step} -- NEXT in {string} | {index} {char} {token.value}")
                if self.isMatchToken(char, token):
                    if len(string) - index == 1:
                        print(f"{self.step} MATCHED 3")
                        return True
                    if len(pattern) == 1:
                        print("END OF PATTERN")
                        self.step += 1
                        continue
                    # print(f'{self.step} -- matched next {char} => {token.value} | {self.str_len - len(string) + index} {self.ptrn_len - len(pattern)}')
                    new_pattern = pattern
                    new_pattern[0].is_star = False
                    result = self.shift(string[index:], new_pattern)
                    if result:
                        print(f"{self.step} MATCHED 4")
                        return True
                else:
                    # print(f'{self.step } -- not matched next {char} => {token.value} | {self.str_len - len(string) + index} {self.ptrn_len - len(pattern)}')
                    # result = self.shift(string[(index):], pattern[1:])
                    return False

            print(f"{self.step} NOT MATCHED")
            self.step += 1
            return False
        else:
            # print(f'{self.step } -- single next {self.step} {char} => {token.value} | {self.str_len - len(string) + 1} {self.ptrn_len - len(pattern) + 1}')
            return self.shift(string[1:], pattern[1:])

    def isMatchToken(self, char: str, token: Token) -> bool:
        return token.value == char or token.value == "."

    def tokenize(self, pattern: str) -> list[Token]:
        tokens = []

        for i in range(len(pattern)):
            if pattern[i] == "*":
                tokens[-1].is_star = True
            else:
                tokens.append(Token(pattern[i], False))

        return tokens

    def toStr(self, tokens: list[Token]) -> str:
        result = ""
        for token in tokens:
            result += f"{token.value + '*' if token.is_star else token.value}"
        return result


s = Solution()
# s.isMatch("aaa", "ab*ac*a")
# s.isMatch("aab", "c*a*b")
# s.isMatch("mississippi", "mis*is*p.")
