"""
Given a string s, find the length of the longest 
substring without repeating characters.

---------------
speed
O(n)

memory
O(1)
"""


class Solution:
    def length_of_longest_substring(self, s: str) -> int:
        len_max_str = 0

        current_str = ""
        for i in range(len(s)):
            if s[i] not in current_str:
                current_str += s[i]
            else:
                if len_max_str < len(current_str):
                    len_max_str = len(current_str)

                current_str = current_str[current_str.find(s[i]) + 1:] + s[i]


print(Solution().length_of_longest_substring("addcb"))
