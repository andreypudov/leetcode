# 169. Majority Element
#
# Given an array nums of size n, return the majority element.
#
# The majority element is the element that appears more than ⌊n / 2⌋ times.
# You may assume that the majority element always exists in the array.

from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = 0

        for value in nums:
            if count == 0:
                candidate = value

            if candidate == value:
                count += 1
            else:
                count -= 1

        return candidate
