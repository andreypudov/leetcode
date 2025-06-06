# 1. Two Sum
#
# Given an array of integers nums and an integer target, return indices of the
# two numbers such that they add up to target. You may assume that each input
# would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.
#
# Constraints:
#
# - 2 <= nums.length <= 10^4
# - -10^9 <= nums[i] <= 10^9
# - -10^9 <= target <= 10^9
# - Only one valid answer exists.

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}

        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_dict:
                return [num_dict[complement], i]
            num_dict[num] = i

        return []
