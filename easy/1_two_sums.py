"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

---------------
speed
O(n)

memory
O(k)
"""

from typing import List


class Solution:
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        lenght = len(nums)

        sums = dict()
        for i in range(lenght):
            second_addend = target - nums[i]
            if second_addend in sums:
                return [sums[second_addend], i]
            else:
                sums[nums[i]] = i
