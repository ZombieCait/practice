class Solution:
    def isPalindrome(self, x: int) -> bool:
        reverse = 0
        tmp = x

        while tmp > 0:
            reverse = reverse * 10 + tmp % 10
            tmp //= 10
        
        if x == reverse:
            return True

        return False

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if str(x) == str(x)[::-1]:
            return True

        return False