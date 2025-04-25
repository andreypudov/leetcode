# 189. Rotate Array
#
# Given an integer array nums, rotate the array to the right by k steps, where
# k is non-negative.

from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        # [1, 2, 3, 4, 5] x 2
        #   s: 1, &t: 3  ::  [1, 2, 3, 4, 5] -> [1, 2, 1, 4, 5]  ::  m = 3
        #   s: m, &t: 5  ::  [1, 2, 1, 4, 5] -> [1, 2, 1, 4, 3]  ::  m = 5
        #   s: m, &t: 2  ::  [1, 2, 1, 4, 3] -> [1, 5, 1, 4, 3]  ::  m = 2
        #   s: m, &t: 4  ::  [1, 5, 1, 4, 3] -> [1, 5, 1, 2, 3]  ::  m = 4
        #   s: m, &t: 1  ::  [1, 5, 1, 2, 3] -> [4, 5, 1, 2, 3]
        #
        #
        # [1, 2, 3, 4, 5] x 3
        #   s: 1, &t: 4  ::  [1, 2, 3, 4, 5] -> [1, 2, 3, 1, 5]  ::  m = 4
        #   s: m, &t: 2  ::  [1, 2, 3, 1, 5] -> [1, 4, 3, 1, 5]  ::  m = 2
        #   s: m, &t: 5  ::  [1, 4, 3, 1, 5] -> [1, 4, 3, 1, 2]  ::  m = 5
        #   s: m, &t: 3  ::  [1, 4, 3, 1, 2] -> [1, 4, 5, 1, 2]  ::  m = 3
        #   s: m, &t: 1  ::  [1, 4, 5, 1, 2] -> [3, 4, 5, 1, 2]
        #
        #
        # [-1, -100, 3, 99] x 2
        #   s: 1, &t: 3  ::  [-1, -100, 3, 99] -> [-1, -100, -1, 99]  ::  m = 3
        #   s: m, &t: 1  ::  [-1, 100, -1, 99] -> [3, 100, -1, 99]    ::  m = -1
        #   s: m, &t: 3  ::  [3, 100, -1, 99]  -> [3, 100, -1, 99]    ::  m = -1
        #   ....
        #
        #   1)
        #     s: 1, &t: 2  ::  [-1, 100, 3, 99] -> [-1, -1, 3, 99]   ::  m = 100
        #     s: m, &t: 3  ::  [-1, -1, 3, 99] -> [-1, -1, 100, 99]  ::  m = 3
        #     s: m, &t: 4  ::  [-1, -1, 100, 99] -> [-1, -1, 100, 3]  ::  m = 99
        #     s: m, &t: 1  ::  [-1, -1, 100, 3] -> [99, -1, 100, 3]
        #   2) ...

        length = len(nums)
        shift = k % length

        if shift == 0 or length <= 1:
            return

        count = 0
        start = 0
        while count < length:
            source = start
            previous = nums[start]

            while True:
                target = (source + shift) % length
                nums[target], previous = previous, nums[target]
                source = target
                count += 1

                if start == source:
                    break

            start += 1
