from typing import List


class Solution:
    def find_median_sorted_arrays(self, nums1: List[int], nums2: List[int]) -> float:
        sorted_nums = sorted(nums1 + nums2)
        middle = int(len(sorted_nums) / 2)

        if len(sorted_nums) % 2 == 1:
            return sorted_nums[middle]
        else:
            return (sorted_nums[middle - 1] + sorted_nums[middle]) / 2


print(Solution().find_median_sorted_arrays([1, 2], [3]))
