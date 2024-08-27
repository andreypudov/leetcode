# 8. String to Integer (atoi)
#
# Implement the myAtoi(string s) function, which converts a string to a 32-bit
# signed integer (similar to C/C++'s atoi function).
#
# The algorithm for myAtoi(string s) is as follows:
#
# 1. Read in and ignore any leading whitespace.
# 2. Check if the next character (if not already at the end of the string) is
#    '-' or '+'. Read this character in if it is either. This determines if the
#    final result is negative or positive respectively. Assume the result is
#    positive if neither is present.
# 3. Read in next the characters until the next non-digit character or the end
#    of the input is reached. The rest of the string is ignored.
# 4. Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If
#    no digits were read, then the integer is 0. Change the sign as necessary
#    (from step 2).
# 5. If the integer is out of the 32-bit signed integer range [-231, 231 - 1],
#    then clamp the integer so that it remains in the range. Specifically,
#    integers less than -231 should be clamped to -231, and integers greater
#    than 231 - 1 should be clamped to 231 - 1.
# 6. Return the integer as the final result.
#
# Note:
#
# - Only the space character ' ' is considered a whitespace character.
# - Do not ignore any characters other than the leading whitespace or the rest
#   of the string after the digits
#
# Constraints:
#
# - 0 <= s.length <= 200
# - s consists of English letters (lower-case and upper-case), digits (0-9),
#   ' ', '+', '-', and '.'.


class Solution:
    def myAtoi(self, string: str) -> int:
        string = self.__trim(string)
        if not string:
            return 0

        is_negative = False
        if string[0] == "-":
            is_negative = True
            string = string[1:]
        elif string[0] == "+":
            string = string[1:]

        result = self.__parse(string, is_negative)
        return result

    def __trim(self, string: str) -> str:
        for index, character in enumerate(string):
            if character != " ":
                return string[index:]

    def __parse(self, string: str, is_negative: bool) -> int:
        result = 0

        for character in string:
            if not character.isdigit():
                break
            result = result * 10 + int(character)

        return max(-(2**31), -result) if is_negative else min(2**31 - 1, result)
