from typing import List

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result = list()
        for i in range(1, n+1):
            if (i % 3 == 0) & (i % 5 == 0):
                result.append('FizzBuzz')
            elif i % 3 == 0:
                result.append('Fizz')
            elif i % 5 == 0:
                result.append('Buzz')
            else:
                result.append(str(i))
        return result


print(Solution().fizzBuzz(3))
print(Solution().fizzBuzz(5))
print(Solution().fizzBuzz(15))