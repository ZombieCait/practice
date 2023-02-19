class Solution:
    def mySqrt(self, x: int) -> int:

        l, r = 0, len(range(x))

        while l < r:
            m = (l + r + 1 ) // 2

            if m * m <= x:
                l = m
            else:
                r = m - 1

        return l

print(Solution().mySqrt(9))
print(Solution().mySqrt(4))
print(Solution().mySqrt(0))
print(Solution().mySqrt(100))