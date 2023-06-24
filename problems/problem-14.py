from typing import List


class Solution:

    def longestCommonPrefix(self, strs: List[str]) -> str:
        first_str = strs[0]
        same_str = ''
        for i in range(0, len(first_str)):
            if not self.isSameSymbol(i, strs):
                break
            same_str += first_str[i]
        print(same_str)
        return same_str

    def isSameSymbol(self, indx, strs):
        symbol = strs[0][indx]
        for string in strs:
            if len(string) < indx + 1:
                return False
            if string[indx] != symbol:
                return False
        return True
