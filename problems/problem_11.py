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

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        unique_height = set(height)
        sorted_height = sorted(unique_height)

        maximum_volume = 0
        left = 0
        right = len(height) - 1

        for level in sorted_height:
            while height[left] < level and left < right:
                left += 1

            while height[right] < level and right > left:
                right -= 1

            current_volume = level * (right - left)
            if current_volume > maximum_volume:
                maximum_volume = current_volume

        return maximum_volume
