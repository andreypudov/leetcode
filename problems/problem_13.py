# 13. Roman to Integer
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
# For example, 2 is written as II in Roman numeral, just two ones added
# together. 12 is written as XII, which is simply X + II. The number 27 is
# written as XXVII, which is XX + V + II.
#
# Roman numerals are usually written largest to smallest from left to right.
# However, the numeral for four is not IIII. Instead, the number four is written
# as IV. Because the one is before the five we subtract it making four. The same
# principle applies to the number nine, which is written as IX. There are six
# instances where subtraction is used:
#
#    I can be placed before V (5) and X (10) to make 4 and 9.
#    X can be placed before L (50) and C (100) to make 40 and 90.
#    C can be placed before D (500) and M (1000) to make 400 and 900.
#
# Given a roman numeral, convert it to an integer.
#
# Constraints:
#
# - 1 <= s.length <= 15
# - s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
# - It is guaranteed that s is a valid roman numeral in the range [1, 3999].


class Solution:
    def romanToInt(self, string: str) -> int:
        number = 0
        index = 0

        while index < len(string):
            next_pair = self.__get_next_token(string, index)
            if next_pair[0] == "M":
                number += 1000
                index += 1
            elif next_pair == "CM":
                number += 900
                index += 2
            elif next_pair[0] == "D":
                number += 500
                index += 1
            elif next_pair == "CD":
                number += 400
                index += 2
            elif next_pair[0] == "C":
                number += 100
                index += 1
            elif next_pair == "XC":
                number += 90
                index += 2
            elif next_pair[0] == "L":
                number += 50
                index += 1
            elif next_pair == "XL":
                number += 40
                index += 2
            elif next_pair[0] == "X":
                number += 10
                index += 1
            elif next_pair == "IX":
                number += 9
                index += 2
            elif next_pair[0] == "V":
                number += 5
                index += 1
            elif next_pair == "IV":
                number += 4
                index += 2
            elif next_pair[0] == "I":
                number += 1
                index += 1

        return number

    def __get_next_token(self, s, pos):
        length = len(s)

        if length - pos >= 2:
            return s[pos : pos + 2]
        else:
            return s[pos : pos + 1]
