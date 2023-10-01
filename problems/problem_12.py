# 12. Integer to Roman
#
# Roman numerals are represented by seven different symbols: I, V, X, L, C, D
# and M.
#
# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
#
# For example, 2 is written as II in Roman numeral, just two one's added
# together. 12 is written as XII, which is simply X + II. The number 27 is
# written as XXVII, which is XX + V + II.
#
# Roman numerals are usually written largest to smallest from left to right.
# However, the numeral for four is not IIII. Instead, the number four is
# written as IV. Because the one is before the five we subtract it making four.
# The same principle applies to the number nine, which is written as IX.
# There are six instances where subtraction is used:
#
# - I can be placed before V (5) and X (10) to make 4 and 9.
# - X can be placed before L (50) and C (100) to make 40 and 90.
# - C can be placed before D (500) and M (1000) to make 400 and 900.
#
# Given an integer, convert it to a roman numeral.
#
# Constraints:
#
# - 1 <= num <= 3999


class Solution:
    def intToRoman(self, num: int) -> str:
        if num < 1 or num > 3999:
            return ""

        if num >= 1000:
            return "M" + self.intToRoman(num - 1000)
        elif num >= 900:
            return "CM" + self.intToRoman(num - 900)
        elif num >= 500:
            return "D" + self.intToRoman(num - 500)
        elif num >= 400:
            return "CD" + self.intToRoman(num - 400)

        elif num >= 100:
            return "C" + self.intToRoman(num - 100)
        elif num >= 90:
            return "XC" + self.intToRoman(num - 90)
        elif num >= 50:
            return "L" + self.intToRoman(num - 50)
        elif num >= 40:
            return "XL" + self.intToRoman(num - 40)

        elif num >= 10:
            return "X" + self.intToRoman(num - 10)
        elif num >= 9:
            return "IX" + self.intToRoman(num - 9)
        elif num >= 5:
            return "V" + self.intToRoman(num - 5)
        elif num >= 4:
            return "IV" + self.intToRoman(num - 4)

        elif num >= 1:
            return "I" + self.intToRoman(num - 1)
