# 14. Longest Common Prefix
#
# Write a function to find the longest common prefix string amongst an array of
# strings. If there is no common prefix, return an empty string "".
#
# Constraints:
#
# - 1 <= strs.length <= 200
# - 0 <= strs[i].length <= 200
# - strs[i] consists of only lowercase English letters.


from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        first_str = strs[0]
        same_str = ""

        for index in range(0, len(first_str)):
            if not self.__is_same_symbol(index, strs):
                break
            same_str += first_str[index]

        return same_str

    def __is_same_symbol(self, index, strs):
        symbol = strs[0][index]

        for string in strs:
            if len(string) < index + 1:
                return False
            if string[index] != symbol:
                return False

        return True
