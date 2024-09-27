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

        # split the array into negative, zero, and positive parts
        negatives, zeros, positives = self.__split(nums)

        # create a sets for faster lookups
        negatives_set = set(negatives)
        positives_set = set(positives)

        # add opposite pairs of negative and positive numbers
        if len(zeros) > 0:
            for p in positives_set:
                if -p in negatives_set:
                    result.add((-p, 0, p))

        # add zeroes if the source array contains at least three zeroes
        if len(zeros) >= 3:
            result.add((0, 0, 0))

        # add pairs of negative numbers that sum up to zero
        for index in range(len(negatives)):
            for rindex in range(index + 1, len(negatives)):
                if -(negatives[index] + negatives[rindex]) in positives_set:
                    result.add(
                        (
                            negatives[index],
                            negatives[rindex],
                            -(negatives[index] + negatives[rindex]),
                        )
                    )

        # add pairs of positive numbers that sum up to zero
        for index in range(len(positives)):
            for rindex in range(index + 1, len(positives)):
                if -(positives[index] + positives[rindex]) in negatives_set:
                    result.add(
                        (
                            -(positives[index] + positives[rindex]),
                            positives[index],
                            positives[rindex],
                        )
                    )

        return list(map(list, result))

    def __split(self, nums: List[int]) -> [List[int], List[int], List[int]]:
        negatives = []
        zeros = []
        positives = []

        for n in nums:
            if n < 0:
                negatives.append(n)
            elif n == 0:
                zeros.append(n)
            else:
                positives.append(n)

        return negatives, zeros, positives
