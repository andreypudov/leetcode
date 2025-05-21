# 217. Contains Duplicate
#
# Given an integer array nums, return true if any value appears at least twice
# in the array, and return false if every element is distinct.
#
# Constraints:
#
# - 1 <= nums.length <= 10^5
# - -10^9 <= nums[i] <= 10^9

from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums_set = set(nums)
        return len(nums_set) != len(nums)
