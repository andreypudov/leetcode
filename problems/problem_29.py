# 29. Divide Two Integers
#
# Given two integers dividend and divisor, divide two integers without using
# multiplication, division, and mod operator.
#
# The integer division should truncate toward zero, which means losing its
# fractional part. For example, 8.345 would be truncated to 8, and -2.7335 would
# be truncated to -2.
#
# Return the quotient after dividing dividend by divisor.
#
# Note: Assume we are dealing with an environment that could only store integers
# within the 32-bit signed integer range: [−2^31, 2^31 − 1]. For this problem,
# if the quotient is strictly greater than 2^31 - 1, then return 2^31 - 1, and
# if the quotient is strictly less than -2^31, then return -2^31.
#
# Constraints:
#
# - -2^31 <= dividend, divisor <= 2^31 - 1
# - divisor != 0


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sign = -1 if (dividend < 0) ^ (divisor < 0) else 1
        dividend = self.__abs(dividend)
        divisor = self.__abs(divisor)

        if dividend == 0:
            return 0

        if divisor == 0:
            return None

        if dividend == divisor:
            return 1 if sign > 0 else -1

        if dividend < divisor:
            return 0

        division = (
            self.__multiplication_ascent(dividend, divisor)
            if divisor != 1
            else dividend
        )
        division = division if sign > 0 else -division

        if division >= 2**31 - 1:
            division = 2**31 - 1

        if division < -(2**31):
            division - 2**31

        return division

    def __multiplication_ascent(self, dividend: int, divisor: int) -> int:
        multiplier = divisor
        quantity = 1
        half_dividend = self.__half(dividend)

        stack = [(multiplier, quantity)]

        while multiplier <= half_dividend:
            multiplier += multiplier
            quantity = self.__double(quantity)
            stack.append((multiplier, quantity))

        dividend -= multiplier
        while dividend >= divisor:
            pair = self.__get_max_pair(stack, dividend)
            dividend -= pair[0]
            quantity += pair[1]

        return quantity

    def __get_max_pair(
        self, stack: list[(int, int)], dividend: int
    ) -> tuple[int, int]:
        while stack:
            pair = stack.pop()
            if pair[0] <= dividend:
                return pair

    def __abs(self, number: int) -> int:
        return number if number >= 0 else -number

    def __double(self, number: int) -> int:
        return number << 1

    def __half(self, number: int) -> int:
        return number >> 1
