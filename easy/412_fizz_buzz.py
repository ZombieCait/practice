"""
Given an integer n, return a string array answer (1-indexed) where:

answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
answer[i] == "Fizz" if i is divisible by 3.
answer[i] == "Buzz" if i is divisible by 5.
answer[i] == i (as a string) if none of the above conditions are true.
---------------
speed
O(n)

memory
O(k)
"""
from typing import List


class Solution:
    def fizz_buzz(self, n: int) -> List[str]:
        result = list()
        for i in range(1, n + 1):
            if (i % 3 == 0) & (i % 5 == 0):
                result.append("FizzBuzz")
            elif i % 3 == 0:
                result.append("Fizz")
            elif i % 5 == 0:
                result.append("Buzz")
            else:
                result.append(str(i))
        return result


print(Solution().fizz_buzz(3))
print(Solution().fizz_buzz(5))
print(Solution().fizz_buzz(15))
