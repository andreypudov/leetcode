# Given a string s, find the length of the longest substring without repeating
# characters.


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        start = 0
        end = 0
        char_dict = {}

        while end < len(s):
            if s[end] in char_dict:
                start = max(start, char_dict[s[end]] + 1)
            char_dict[s[end]] = end
            longest = max(longest, end - start + 1)
            end += 1

        return longest
