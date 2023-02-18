from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        m = 1

        for i in range(len(nums)-1):
            if nums[i]!=nums[i+1]:
                nums[m] = nums[i+1]
                m += 1

        return m

print(Solution().removeDuplicates([0,0,1,1,1,2,2,3,3,4]))