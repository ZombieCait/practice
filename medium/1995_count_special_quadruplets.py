from itertools import combinations
from typing import List


class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        ans = 0
        for a, b, c, d in combinations(nums, 4):
            if a + b + c == d:
                ans += 1
        return ans


# class Solution:
#     def countQuadruplets(self, nums: List[int]) -> int:
#         nums = sorted(nums)
#         cnt = 0
#         lenght = len(nums)

#         for i in range(lenght):
#             for j in range(i+1, lenght):
#                 l, r = j+1, lenght-1

#                 while l < r:
#                     if nums[i] + nums[j] + nums[l] == nums[r]:
#                         cnt += 1
#                         l += 1
#                         r -= 1
#                     elif nums[i] + nums[j] + nums[l] - nums[r] > 0:
#                         r -= 1
#                     else:
#                         l += 1
#         return cnt
