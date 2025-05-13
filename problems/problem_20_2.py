# 20. Valid Parentheses
#
# Given a string s containing just the characters '(', ')', '{', '}', '[' and
# ']', determine if the input string is valid.
#
# An input string is valid if:
#
# - Open brackets must be closed by the same type of brackets.
# - Open brackets must be closed in the correct order.
# - Every close bracket has a corresponding open bracket of the same type.


class Solution:
    def _isMatchingBracket(self, previous: str, current: str):
        return (
            (previous == "(" and current == ")")
            or (previous == "{" and current == "}")
            or (previous == "[" and current == "]")
        )

    def isValid(self, s: str) -> bool:
        brackets = []

        for bracket in s:
            if bracket in ["(", "{", "["]:
                brackets.append(bracket)
                continue

            previousBracket = None if len(brackets) == 0 else brackets[-1]
            if self._isMatchingBracket(previousBracket, bracket):
                brackets.pop()
            else:
                return False

        return len(brackets) == 0
