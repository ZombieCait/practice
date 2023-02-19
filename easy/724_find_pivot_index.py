from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        SUM = sum(nums)
        leftsum = 0
        
        for i, n in enumerate(nums):    
            if leftsum == SUM - leftsum - n:
                return i
            leftsum += n

        return -1

print(Solution().pivotIndex([1,7,3,6,5,6]))