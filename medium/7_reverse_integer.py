class Solution:
    def reverse(self, x: int) -> int:
        result = str(abs(x))[::-1]
        symbol = -1 if x < 1 else 1
        return int(result) * symbol if  result <= 2 ** 31 else 0

class Solution:
    def reverse(self, x: int) -> int:
        result, symbol = 0, 1

        if x < 0:
            symbol = -1
            x = -x
            
        while x>0:
            result = result * 10 + x % 10
            x //= 10

        return result * symbol if result < 2 ** 31 else 0