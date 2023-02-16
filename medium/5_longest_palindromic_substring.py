class Solution:
    def longestPalindrome(self, s: str) -> str:
        lengh = len(s)
        longest_palindrome_start, longest_palindrome_len = 0, 1

        for i in range(0, lengh):
            right = i
            while (right < lengh) and (s[i] == s[right]):
                right += 1

            left = i - 1 
            while (left >= 0) and (right < lengh) and (s[left] == s[right]):
                left -= 1
                right +=1

            
            palindrome_len = right - left - 1
            if palindrome_len > longest_palindrome_len:
                longest_palindrome_len = palindrome_len
                longest_palindrome_start = left + 1 
        
        return s[longest_palindrome_start: longest_palindrome_start + longest_palindrome_len]