"""
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.
---------------
speed
O(n)

memory
O(1)
"""

from typing import List


class Solution:
    def running_sum(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            nums[i] = nums[i - 1] + nums[i]

        return nums


print(Solution().running_sum([1, 2, 3, 4]))
