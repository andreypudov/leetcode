# 42. Trapping Rain Water
#
# Given n non-negative integers representing an elevation map where the width
# of each bar is 1, compute how much water it can trap after raining.

from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        summit = max(height)
        volume = 0
        length = len(height)

        left = -1
        right = -1

        for level in range(summit):
            bars = [1 if bar > level else 0 for bar in height]

            for bar in range(length):
                if bars[bar] != 0:
                    left = bar
                    break

            for bar in range(length - 1, -1, -1):
                if bars[bar] != 0:
                    right = bar
                    break

            volume += bars[left : right + 1].count(0)

        return volume
