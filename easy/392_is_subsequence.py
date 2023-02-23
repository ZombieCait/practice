class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False

        i, j = 0, 0
        t_lenght = len(t)
        s_lenght = len(s)

        while i < t_lenght:
            if j == s_lenght:
                return True

            if t[i] == s[j]:
                j += 1

            i += 1

        if j == s_lenght:
            return True

        return False


print(Solution().isSubsequence("abc", "ahbgdc"))
print(Solution().isSubsequence("", "ahbgdc"))
print(Solution().isSubsequence("abc", "adc"))
print(Solution().isSubsequence("abc", ""))
print(Solution().isSubsequence("", ""))
