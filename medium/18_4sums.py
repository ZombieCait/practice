from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        quadruplets  = []
        nums = sorted(nums)

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                l, r = j + 1, len(nums) - 1
                rest =  target - nums[i] - nums[j]

                while l < r:
                    if rest == nums[l] + nums[r]:
                        quadruplet = sorted([nums[i], nums[j], nums[l], nums[r]])
                        l += 1
                        r -= 1
                        if quadruplet not in quadruplets:
                            quadruplets.append(quadruplet)

                        while nums[l]==quadruplet[2]  and l < r :
                            l+=1
                        while nums[r]==quadruplet[3] and l < r:
                            r-=1
                    elif rest < nums[l] + nums[r]:
                        r -= 1
                    else:
                        l += 1
                        
            
        return quadruplets

Solution().fourSum([1,0,-1,0,-2,2], 0)