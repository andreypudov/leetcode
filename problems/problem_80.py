# 80. Remove Duplicates from Sorted Array II
#
# Given an integer array nums sorted in non-decreasing order, remove some
# duplicates in-place such that each unique element appears at most twice.
# The relative order of the elements should be kept the same.
#
# Since it is impossible to change the length of the array in some languages,
# you must instead have the result be placed in the first part of the array
# nums. More formally, if there are k elements after removing the duplicates,
# then the first k elements of nums should hold the final result. It does not
# matter what you leave beyond the first k elements.
#
# Return k after placing the final result in the first k slots of nums.
#
# Do not allocate extra space for another array. You must do this by modifying
# the input array in-place with O(1) extra memory.
#
# Custom Judge:
#
# The judge will test your solution with the following code:
#
# int[] nums = [...]; // Input array
# int[] expectedNums = [...]; // The expected answer with correct length
#
# int k = removeDuplicates(nums); // Calls your implementation
#
# assert k == expectedNums.length;
# for (int i = 0; i < k; i++) {
#     assert nums[i] == expectedNums[i];
# }
#
# If all assertions pass, then your solution will be accepted.

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)

        current_value = nums[0]
        occurrence = 1

        write_index = 1
        read_index = 1

        while read_index < len(nums):
            if nums[read_index] == current_value:
                occurrence += 1
            else:
                current_value = nums[read_index]
                occurrence = 1

            if occurrence > 2:
                read_index += 1
                continue

            nums[write_index] = nums[read_index]

            write_index += 1
            read_index += 1

        return write_index
