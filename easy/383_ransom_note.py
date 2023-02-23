"""
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.
---------------
speed
O(n)

memory
O(n)
"""


class Solution:
    def can_construct(self, ransomNote: str, magazine: str) -> bool:
        magazine = list(magazine)
        for letter in ransomNote:
            try:
                magazine.remove(letter)
            except:
                return False

        return True


print(Solution().can_construct("aa", "ab"))
print(Solution().can_construct("aa", "aab"))
print(Solution().can_construct("a", "b"))
