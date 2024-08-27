# Given a string s, return the longest palindromic substring in s.


class Solution:
    def longestPalindrome(self, s: str) -> str:
        palindrom = ""
        length = 0

        for index in range(len(s)):
            cur_palindrom = self.__get_palindrom(s[index:])
            cur_length = len(cur_palindrom)

            if cur_length > length:
                palindrom = cur_palindrom
                length = cur_length

        return palindrom

    def __get_palindrom(self, s: str) -> str:
        palindrom = ""

        for index in range(len(s), 0, -1):
            sub = s[0:index]
            if self.__is_palindrom(sub):
                palindrom = sub
                break

        return palindrom

    def __is_palindrom(self, s: str) -> bool:
        return s == s[::-1]
