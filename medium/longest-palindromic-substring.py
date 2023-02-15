class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_str_palindrom = ''

        for i, j in zip(s, s[::-1]):
            while s[i]
            max_str_palindrom += s[i]

        return s


print(Solution().longestPalindrome('babad'))