# Given two sorted arrays nums1 and nums2 of size m and n respectively, return
# the median of the two sorted arrays. The overall run time complexity should
# be O(log (m+n)).

from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = self.merge(nums1, nums2)
        return self.getMedian(merged)

    def merge(self, nums1: List[int], nums2: List[int]) -> List[int]:
        merged = []
        i = 0
        j = 0

        while i < len(nums1) or j < len(nums2):
            if i < len(nums1) and j < len(nums2):
                if nums1[i] <= nums2[j]:
                    merged.append(nums1[i])
                    i += 1
                else:
                    merged.append(nums2[j])
                    j += 1
            elif i < len(nums1):
                merged.append(nums1[i])
                i += 1
            elif j < len(nums2):
                merged.append(nums2[j])
                j += 1

        return merged

    def getMedian(self, nums: List[int]) -> float:
        length = len(nums)
        if length % 2 == 0:
            return (nums[length // 2 - 1] + nums[length // 2]) / 2
        else:
            return nums[length // 2]
