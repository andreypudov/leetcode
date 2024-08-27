# Write a function to find the longest common prefix string amongst an array of
# strings. If there is no common prefix, return an empty string "".

from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        first_str = strs[0]
        same_str = ""

        for i in range(0, len(first_str)):
            if not self.__is_same_symbol(i, strs):
                break
            same_str += first_str[i]

        return same_str

    def __is_same_symbol(self, indx, strs):
        symbol = strs[0][indx]

        for string in strs:
            if len(string) < indx + 1:
                return False
            if string[indx] != symbol:
                return False

        return True
