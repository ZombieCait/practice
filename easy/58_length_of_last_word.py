class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.strip().split(' ')[-1])

s = "   fly me   to   the moon  "
print(Solution().lengthOfLastWord(s))