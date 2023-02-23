from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        closest_sum = 10**5
        nums = sorted(nums)

        for i, first in enumerate(nums):
            if i > 0 and first == nums[i - 1]:
                continue

            left, right = i + 1, len(nums) - 1

            while left < right:
                triplet = [first, nums[left], nums[right]]
                res = sum(triplet)
                if abs(target - closest_sum) > abs(target - res):
                    closest_sum = res

                if res > target:
                    right -= 1
                elif res < target:
                    left += 1
                else:
                    closest_sum = res

                    while nums[left] == triplet[1] and left < right:
                        left += 1
                    while nums[right] == triplet[2] and left < right:
                        right -= 1

        return closest_sum
