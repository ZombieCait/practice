from inspect import stack


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine = list(magazine)
        for letter in ransomNote:
            try:
                magazine.remove(letter)
            except:
                return False
                
        return True




print(Solution().canConstruct('aa', 'ab'))
print(Solution().canConstruct('aa', 'aab'))
print(Solution().canConstruct('a', 'b'))