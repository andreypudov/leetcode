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


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sign = -1 if (dividend < 0) ^ (divisor < 0) else 1
        dividend = self.abs(dividend)
        divisor = self.abs(divisor)

        if dividend == 0:
            return 0

        if divisor == 0:
            return None

        if dividend == divisor:
            return 1 if sign > 0 else -1

        if dividend < divisor:
            return 0

        division = (
            self.multiplicationAscent(dividend, divisor) if divisor != 1 else dividend
        )
        division = division if sign > 0 else -division

        if division >= 2**31 - 1:
            division = 2**31 - 1

        if division < -(2**31):
            division - 2**31

        return division

    def multiplicationAscent(self, dividend: int, divisor: int) -> dict[int, int]:
        multiplier = divisor
        quantity = 1
        halfDividend = self.half(dividend)

        cache = {multiplier: quantity}

        while multiplier <= halfDividend:
            multiplier += multiplier
            quantity = self.double(quantity)
            cache[multiplier] = quantity

        dividend -= multiplier
        while dividend >= divisor:
            values = max(filter(lambda key: key[0] <= dividend, cache.items()))
            cache[values[0]] = values[1]
            dividend -= values[0]
            quantity += values[1]

        return quantity

    def abs(self, number: int) -> int:
        return number if number >= 0 else -number

    def double(self, number: int) -> int:
        return number << 1

    def half(self, number: int) -> int:
        return number >> 1


instance = Solution()

print("-1 / 1 = -1 =>", instance.divide(-1, 1))
print("1 / -1 = -1 =>", instance.divide(1, -1))
print("-1 / -1 = 1 =>", instance.divide(-1, -1))

print("7 / 2 = 3 =>", instance.divide(7, 2))
print("4 / 3 = 1 =>", instance.divide(4, 3))
print("1 / 2 = 0 =>", instance.divide(1, 2))

print("1024 / 3 = 341 =>", instance.divide(1024, 3))
print("2037 / 3 = 679 =>", instance.divide(2037, 3))
print("2^32 / 6 = 715827882 =>", instance.divide(2**32, 6))

print("2147483648 / 1 = 2147483647 =>", instance.divide(2147483648, 1))
print("-2147483648 / -1 = 2147483647 =>", instance.divide(-2147483648, -1))
print("-2147483648 / 1 = -2147483648 =>", instance.divide(-2147483648, 1))
