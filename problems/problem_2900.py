from multiprocessing.connection import answer_challenge
from typing import List


# class Solution:
#     def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
#         prev_group = None
#         answer = []
#         for index, group in enumerate(groups):
#             if group != prev_group:
#                 answer.append(words[index])
#             prev_group = group
#         return answer


class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        prev_group = None
        shift = 0
        for index, group in enumerate(groups):
            if group == prev_group:
                words.pop(index - shift)
                shift += 1
            prev_group = group
        return words
