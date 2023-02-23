"""
Given an integer num, return the number of steps to reduce it to zero.

In one step, if the current number is even, you have to divide it by 2, otherwise, you have to subtract 1 from it.
---------------
speed
O(n)

memory
O(1)
"""


class Solution:
    def number_of_steps(self, num: int) -> int:
        steps = 0
        while num != 0:
            if num % 2 == 0:
                num = num / 2
            else:
                num -= 1

            steps += 1

        return steps


print(Solution().number_of_steps(14))
