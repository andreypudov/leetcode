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
        closest = float("inf")

        nums.sort()

        for index in range(len(nums)):
            start = index + 1
            end = len(nums) - 1
            current = nums[index]

            while start < end:
                sum = current + nums[start] + nums[end]
                closest = self.__update_closest(closest, sum, target)

                if sum == target:
                    return sum
                elif sum < target:
                    start += 1
                else:
                    end -= 1

        return closest

    def __update_closest(self, closest: int, sum: int, target: int) -> int:
        if abs(target - sum) < abs(target - closest):
            return sum

        return closest
