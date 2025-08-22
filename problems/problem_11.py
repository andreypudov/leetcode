# 11. Container With Most Water
#
# You are given an integer array height of length n. There are n vertical
# lines drawn such that the two endpoints of the ith line are (i, 0) and
# (i, height[i]).
#
# Find two lines that together with the x-axis form a container, such that the
# container contains the most water.
#
# Return the maximum amount of water a container can store.
#
# Notice that you may not slant the container.

from itertools import groupby
from operator import itemgetter
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        indexed_height = list(enumerate(height))
        sorted_height = sorted(indexed_height, key=lambda arr: arr[1])
        grouped_height = [
            list(v) for _, v in groupby(sorted_height, key=itemgetter(1))
        ]

        print(" :: ", grouped_height)

        max_amount = 0

        for index in range(len(sorted_height) - 1, 0, -1):
            print(" >> ", index)

            right_bar = sorted_height[index]
            left_bar = sorted_height[index - 1]

            distance = abs(right_bar[0] - left_bar[0])
            height = min(right_bar[1], left_bar[1])

            current_amount = distance * height
            if current_amount > max_amount:
                max_amount = current_amount

        return max_amount
