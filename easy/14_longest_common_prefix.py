"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
---------------
speed
O(n)

memory
O(k)
"""
import re
from typing import List


class Solution:
    def longest_common_prefix(self, strs: List[str]) -> str:
        res = ""
        for a in zip(*strs):
            if len(set(a)) == 1:
                res += a[0]
            else:
                return res
        return res


print(Solution().longest_common_prefix(["flower", "flow", "flight"]))
print(Solution().longest_common_prefix(["dog", "racecar", "car"]))
