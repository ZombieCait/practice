"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
---------------
speed
O(n)

memory
O(k)
"""


class Solution:
    def is_valid(self, s: str) -> bool:
        stack = list()

        parentheses = {")": "(", "]": "[", "}": "{"}

        for symbol in s:
            if symbol in "({[":
                stack.append(symbol)
            else:
                if len(stack) != 0:
                    if stack.pop() != parentheses[symbol]:
                        return False
                else:
                    return False

        return stack == []


print(Solution().is_valid("()"))
print(Solution().is_valid("()[]{}"))
print(Solution().is_valid("(]"))
print(Solution().is_valid(""))
print(Solution().is_valid("()]"))
print(Solution().is_valid("[(()]"))
