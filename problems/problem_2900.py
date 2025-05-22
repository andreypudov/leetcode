# 2900. Longest Unequal Adjacent Groups Subsequence I
#
# You are given a string array words and a binary array groups both of
# length n.
#
# A subsequence of words is alternating if for any two consecutive strings in
# the sequence, their corresponding elements at the same indices in groups are
# different (that is, there cannot be consecutive 0 or 1).
#
# Your task is to select the longest alternating subsequence from words.
#
# Return the selected subsequence. If there are multiple answers, return any
# of them.
#
# Note: The elements in words are distinct.

from typing import List


class Solution:
    def getLongestSubsequence(
        self, words: List[str], groups: List[int]
    ) -> List[str]:
        prev_group = None
        shift = 0
        for index, group in enumerate(groups):
            if group == prev_group:
                words.pop(index - shift)
                shift += 1
            prev_group = group
        return words
