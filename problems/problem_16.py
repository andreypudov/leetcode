# 16. 3Sum Closest
#
# Given an integer array nums of length n and an integer target, find three
# integers in nums such that the sum is closest to target.
#
# Return the sum of the three integers.
#
# You may assume that each input would have exactly one solution.

from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        closest_sum = float("inf")

        nums.sort()

        for index in range(len(nums)):
            start = index + 1
            end = len(nums) - 1

            while start < end:
                current_sum = nums[index] + nums[start] + nums[end]

                if abs(target - current_sum) < abs(target - closest_sum):
                    closest_sum = current_sum

                if current_sum < target:
                    start += 1
                elif current_sum > target:
                    end -= 1
                else:
                    return current_sum

        return closest_sum
