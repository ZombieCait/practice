class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lenght = len(nums)

        sums = dict()
        for i in range(lenght):
            second_addend = target - nums[i]
            if second_addend in sums:
                return [sums[second_addend], i]
            else:
                sums[nums[i]] = i