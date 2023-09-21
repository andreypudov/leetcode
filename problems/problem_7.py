# Given a signed 32-bit integer x, return x with its digits reversed. If
# reversing x causes the value to go outside the signed 32-bit integer range
# [-231, 231 - 1], then return 0.
#
# Assume the environment does not allow you to store 64-bit integers (signed or
# unsigned).

import math


class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0

        getReversedDigits = self.getReversedDigits(abs(x))
        number = self.getNumber(getReversedDigits)
        number = number * (-1) if x < 0 else number

        if number >= 2**31 - 1 or number <= (2**31 + 1) * (-1):
            return 0

        return number

    def getReversedDigits(self, x: int) -> int:
        numDigits = math.floor(math.log10(abs(x))) + 1
        digitList = [0] * numDigits
        currentPos = 0

        while x > 9:
            mod = x % 10
            digitList[currentPos] = mod
            x = int(x / 10)
            currentPos += 1

        digitList[currentPos] = x

        return digitList

    def getNumber(self, digitList):
        number = 0
        pos = 1

        for indx in range(len(digitList) - 1, -1, -1):
            number += digitList[indx] * pos
            pos *= 10

        return number


sol = Solution()
print(sol.reverse(123))
