from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        def add_one(i, digits):
            if -i > lenght:
                digits.insert(0, 1)
            elif digits[i] < 9:
                digits[i] += 1
            else:
                digits[i] = 0
                add_one(i-1, digits)
                

        lenght = len(digits)
        add_one(-1, digits)

        return digits

#faster
class Solution2:
    def plusOne(self, digits: List[int]) -> List[int]:              
        for i in range(len(digits)-1, -1, -1):
            if digits[i] != 9:
                digits[i] += 1
                break
            else:
                digits[i] = 0
                
            
        if digits[0] == 0:
            digits.insert(0, 1)

        return digits

print(Solution().plusOne([9]))

print(Solution2().plusOne([9]))