"""
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.
------------------
time
O(n)

memory
O(k+n)
"""


class Solution:
    def is_isomorphic(self, s: str, t: str) -> bool:
        d1 = {}
        d2 = {}

        for i in range(len(t)):
            if s[i] not in d1.keys() and t[i] not in d2.keys():
                d1[s[i]] = t[i]
                d2[t[i]] = s[i]
            elif d1.get(s[i]) != t[i] or d2.get(t[i]) != s[i]:
                return False

        return True


print(Solution().is_isomorphic("egg", "add"))
print(Solution().is_isomorphic("paper", "title"))
print(Solution().is_isomorphic("foo", "bar"))
