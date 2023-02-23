"""
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
---------------
speed
O(n)

memory
O(1)
"""

from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> List[int]:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1, p2, write_index = m - 1, n - 1, m + n - 1
        while p2 >= 0:
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[write_index] = nums1[p1]
                p1 -= 1
            else:
                nums1[write_index] = nums2[p2]
                p2 -= 1

            write_index -= 1

        return nums1


print(Solution().merge([1, 2, 3, 0, 0, 0], 3, [2, 4, 5], 3))
print(Solution().merge([1], 1, [], 0))
print(Solution().merge([0], 0, [1], 1))
print(Solution().merge([4, 5, 6, 0, 0, 0], 3, [1, 2, 3], 3))
