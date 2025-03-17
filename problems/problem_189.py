# 189. Rotate Array
#
# Given an integer array nums, rotate the array to the right by k steps, where
# k is non-negative.

from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        buffer = [None] * len(nums)
        length = len(nums)
        shift = k % len(nums)

        begin_dst = shift
        end_dst = length
        begin_src = 0
        end_src = end_dst - begin_dst

        buffer[begin_dst:end_dst] = nums[begin_src:end_src]

        begin_dst = 0
        end_dst = shift
        begin_src = length - shift
        end_src = length

        buffer[begin_dst:end_dst] = nums[begin_src:end_src]

        nums[0:length] = buffer[0:length]
