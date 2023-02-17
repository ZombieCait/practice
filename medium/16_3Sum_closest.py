class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        closest_sum = 10 ** 5
        nums = sorted(nums)

        for i, first in enumerate(nums):
            if i>0 and first == nums[i-1]:
                continue
            
            l, r = i+1, len(nums) - 1

            while l < r:
                triplet = [first, nums[l], nums[r]]
                res = sum(triplet)
                if abs(target - closest_sum) > abs(target - res):
                    closest_sum = res

                if res > target:
                    r -= 1
                elif res < target:
                    l += 1
                else:
                    closest_sum = res
                          
                    while nums[l]==triplet[1]  and l < r :
                        l+=1
                    while nums[r]==triplet[2] and l < r:
                        r-=1
            
        return closest_sum