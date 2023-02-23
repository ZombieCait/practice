"""
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.
---------------
speed
O(n)

memory
O(1)
"""
from typing import List


class Solution:
    def plus_one(self, digits: List[int]) -> List[int]:
        def add_one(i, digits):
            if -i > lenght:
                digits.insert(0, 1)
            elif digits[i] < 9:
                digits[i] += 1
            else:
                digits[i] = 0
                add_one(i - 1, digits)

        lenght = len(digits)
        add_one(-1, digits)

        return digits


# faster
class Solution2:
    def plus_one(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] != 9:
                digits[i] += 1
                break
            else:
                digits[i] = 0

        if digits[0] == 0:
            digits.insert(0, 1)

        return digits


print(Solution().plus_one([9]))

print(Solution2().plus_one([9]))
