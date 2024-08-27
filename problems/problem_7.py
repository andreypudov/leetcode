# 7. Reverse Integer
#
# Given a signed 32-bit integer x, return x with its digits reversed. If
# reversing x causes the value to go outside the signed 32-bit integer range
# [-231, 231 - 1], then return 0.
#
# Assume the environment does not allow you to store 64-bit integers (signed or
# unsigned).
#
# Constraints:
#
# - -2^31 <= x <= 2^31 - 1


import math


class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0

        reversed_digits = self.__get_reversed_digits(abs(x))
        number = self.__get_number(reversed_digits)
        number = number * (-1) if x < 0 else number

        if number >= 2**31 - 1 or number <= (2**31 + 1) * (-1):
            return 0

        return number

    def __get_reversed_digits(self, x: int) -> int:
        num_digits = math.floor(math.log10(abs(x))) + 1
        digit_list = [0] * num_digits
        current_pos = 0

        while x > 9:
            mod = x % 10
            digit_list[current_pos] = mod
            x = int(x / 10)
            current_pos += 1

        digit_list[current_pos] = x

        return digit_list

    def __get_number(self, digit_list):
        number = 0
        pos = 1

        for index in range(len(digit_list) - 1, -1, -1):
            number += digit_list[index] * pos
            pos *= 10

        return number
