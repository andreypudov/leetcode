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
        nums.sort()

        return self.__k_sum_closest(nums, 3, target)

    def __k_sum_closest(self, nums, k, target):
        # the number of elements is the same as the expected sum length
        if k == len(nums):
            return sum(nums[:k])

        # the target is too low
        current_sum = sum(nums[:k])
        if current_sum >= target:
            return current_sum

        # the target is too high
        current_sum = sum(nums[-k:])
        if current_sum <= target:
            return current_sum

        # find the closest number to the target
        if k == 1:
            deltas = [(value, abs(target - value)) for value in nums]
            closest = min(deltas, key=lambda value: value[1])[0]

            return closest

        # recursive search
        closest_sum = sum(nums[:k])
        for index, value in enumerate(nums[: -k + 1]):
            # handle duplicate values
            if index > 0 and nums[index - 1] == value:
                continue

            current_sum = (
                self.__k_sum_closest(nums[index + 1 :], k - 1, target - value)
                + value
            )
            if abs(target - current_sum) < abs(target - closest_sum):
                if current_sum == target:
                    return current_sum
                else:
                    closest_sum = current_sum

        return closest_sum
