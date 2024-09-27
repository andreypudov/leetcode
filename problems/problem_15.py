# 15. 3Sum
#
# Given an integer array nums, return all the triplets [nums[i], nums[j],
# nums[k]] such that i != j, i != k, and j != k, and
# nums[i] + nums[j] + nums[k] == 0.
#
# Notice that the solution set must not contain duplicate triplets.

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()

        nums.sort()

        for index in range(len(nums)):
            start = index + 1
            end = len(nums) - 1
            current = nums[index]

            while start < end:
                sum = current + nums[start] + nums[end]

                if sum == 0:
                    value = tuple(sorted([current, nums[start], nums[end]]))
                    result.add(value)

                    start += 1
                    end -= 1
                elif sum < 0:
                    start += 1
                else:
                    end -= 1

        return list(map(list, result))
