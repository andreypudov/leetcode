# 42. Trapping Rain Water
#
# Given n non-negative integers representing an elevation map where the width
# of each bar is 1, compute how much water it can trap after raining.

from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        max_value = max(height)
        max_index = [i for i, v in enumerate(height) if v == max_value]

        def get_volume(
            height: List[int], start: int, end: int, direction: int
        ) -> int:
            level = -1
            volume = 0

            for index in range(start, end, direction):
                current_level = height[index]

                if current_level >= level:
                    level = current_level
                else:
                    volume += level - current_level

            return volume

        return (
            get_volume(height, 0, max_index[0], 1)
            + get_volume(height, max_index[0], max_index[-1], 1)
            + get_volume(height, len(height) - 1, max_index[-1], -1)
        )
