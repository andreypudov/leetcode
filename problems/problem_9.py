# Given an integer x, return true if x is a palindrome, and false otherwise.

import math


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        source = x
        reversed = 0

        while x > 0:
            reversed = reversed * 10 + x % 10
            x = math.floor(x / 10)

        return source == reversed
