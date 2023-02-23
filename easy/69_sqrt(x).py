"""
Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.

---------------
speed
O(log n)

memory
O(1)
"""


class Solution:
    def my_sqrt(self, x: int) -> int:

        l, r = 0, len(range(x))

        while l < r:
            m = (l + r + 1) // 2

            if m * m <= x:
                l = m
            else:
                r = m - 1

        return l


print(Solution().my_sqrt(9))
print(Solution().my_sqrt(4))
print(Solution().my_sqrt(0))
print(Solution().my_sqrt(100))
