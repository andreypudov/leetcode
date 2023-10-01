# 5. Longest Palindromic Substring
#
# Given a string s, return the longest palindromic substring in s.
#
# Constraints:
#
# - 1 <= s.length <= 1000
# - s consist of only digits and English letters.


class Solution:
    def longestPalindrome(self, s: str) -> str:
        palindrom = ""
        length = 0

        for index in range(len(s)):
            cur_palindrom = self.getPalindrom(s[index:])
            cur_length = len(cur_palindrom)

            if cur_length > length:
                palindrom = cur_palindrom
                length = cur_length

        return palindrom

    def getPalindrom(self, s: str) -> str:
        palindrom = ""

        for index in range(len(s), 0, -1):
            sub = s[0:index]
            if self.isPalindrom(sub):
                palindrom = sub
                break

        return palindrom

    def isPalindrom(self, s: str) -> bool:
        return s == s[::-1]
