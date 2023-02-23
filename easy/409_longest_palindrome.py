"""
Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome here.

---------------
speed
O(n+k)

memory
O(1)
"""

from collections import Counter


class Solution:
    def longest_palindrome(self, s: str) -> int:
        letters_cnt = Counter(s)

        palindrom_lenght = 0
        one_letter = 1

        for letter, count in letters_cnt.items():
            if one_letter & (count % 2 == 1):
                palindrom_lenght += count
                one_letter = 0
            else:
                palindrom_lenght += (count // 2) * 2

        return palindrom_lenght


print(Solution().longest_palindrome("aaa"))
print(Solution().longest_palindrome("AAaaab"))
print(Solution().longest_palindrome("fgacdhwfwfsffff"))
