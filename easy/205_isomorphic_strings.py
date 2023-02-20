class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d1 = {}
        d2 = {}

        for i in range(len(t)):
            if s[i] not in d1.keys() and t[i] not in d2.keys():
                d1[s[i]] = t[i]
                d2[t[i]] = s[i]
            elif d1.get(s[i]) != t[i] or d2.get(t[i]) != s[i]:
                return False


        return True 



print(Solution().isIsomorphic('egg', 'add'))
print(Solution().isIsomorphic('paper', 'title'))
print(Solution().isIsomorphic('foo', 'bar'))