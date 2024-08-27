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
        palindrome = ""
        length = 0

        for index in range(len(s)):
            cur_palindrome = self.__get_palindrome(s[index:])
            cur_length = len(cur_palindrome)

            if cur_length > length:
                palindrome = cur_palindrome
                length = cur_length

        return palindrome

    def __get_palindrome(self, s: str) -> str:
        palindrome = ""

        for index in range(len(s), 0, -1):
            sub = s[0:index]
            if self.__is_palindrome(sub):
                palindrome = sub
                break

        return palindrome

    def __is_palindrome(self, s: str) -> bool:
        return s == s[::-1]
