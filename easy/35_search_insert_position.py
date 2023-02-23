"""
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.
---------------
speed
O(n)

memory
O(1)
"""

from typing import List


class Solution:
    def search_insert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)

        while l < r:
            m = (l + r) // 2
            if nums[m] >= target:
                r = m
            else:
                l = m + 1
        return l


print(Solution().search_insert([1, 3, 5, 6], 7))
