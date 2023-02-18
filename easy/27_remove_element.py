from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        m = 0

        for i in range(len(nums)):
            if nums[i]!=val:
                nums[m] = nums[i]
                m += 1

        return m

print(Solution().removeElement([0,0,1,1,1,2,2,3,3,4]))