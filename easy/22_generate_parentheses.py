'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

---------------
speed
<O(n)

memory
<O(n)

'''


from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def get_paranthesis(s=[], l=0, r=0):
            if len(s) == 2*n:
                result.append(''.join(s))
                return
            if l < n:
                s.append("(")
                get_paranthesis(s, l + 1, r)
                s.pop()
            if r < l:
                s.append(")")
                get_paranthesis(s, l, r + 1)
                s.pop()
        
        get_paranthesis()
        return result

print(Solution().generateParenthesis(0))

print(Solution().generateParenthesis(7))

print(Solution().generateParenthesis(3))