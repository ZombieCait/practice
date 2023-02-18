from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        nums = sorted(nums)

        for i, first in enumerate(nums):
            if i>0 and first == nums[i-1]:
                continue
            
            l, r = i+1, len(nums) - 1

            while l < r:
                res = first + nums[l] + nums[r]
                if res > 0:
                    r -= 1
                elif res < 0:
                    l += 1
                else:
                    triplet = sorted([first,  nums[l], nums[r]])
                    triplets.append(triplet)
                          
                    while nums[l]==triplet[1]  and l < r :
                        l+=1
                    while nums[r]==triplet[2] and l < r:
                        r-=1
            
        return triplets
        
print(Solution().threeSum([-1,0,1,2,-1,-4,-2,-3,3,0,4]))