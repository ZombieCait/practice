class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        len_max_str = 0

        current_str = ''
        for i in range(len(s)):
            if s[i] not in current_str:
                current_str += s[i]
            else:
                if len_max_str < len(current_str):
                    len_max_str = len(current_str)

                current_str = current_str[current_str.find(s[i])+1:]+s[i]

print(Solution().lengthOfLongestSubstring("addcb"))