# 28. Find the Index of the First Occurrence in a String
#
# Given two strings needle and haystack, return the index of the first
# occurrence of needle in haystack, or -1 if needle is not part of haystack.

from typing import Dict


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0

        if len(haystack) == 0:
            return -1

        shift_table = self.__make_shift_table(needle)
        return self.__find_first(haystack, needle, shift_table)

    def __make_shift_table(self, needle: str) -> Dict[str, int]:
        length = len(needle)
        shift_table = {ch: length for ch in set(needle)}

        for i in range(length - 1):
            shift_table[needle[i]] = length - i - 1

        return shift_table

    def __find_first(
        self, haystack: str, needle: str, shift_table: Dict[str, int]
    ) -> int:
        haystack_len = len(haystack)
        needle_len = len(needle)
        index = needle_len - 1

        while index < haystack_len:
            needle_index = needle_len - 1
            haystack_index = index

            while (
                needle_index >= 0
                and haystack[haystack_index] == needle[needle_index]
            ):
                haystack_index -= 1
                needle_index -= 1

            if needle_index == -1:
                return haystack_index + 1

            shift = shift_table.get(haystack[index], needle_len)
            index += shift

        return -1
