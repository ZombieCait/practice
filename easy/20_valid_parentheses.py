class Solution:
    def isValid(self, s: str) -> bool:
        stack = list()

        parentheses = {
            ')':'(',
            ']':'[',
            '}':'{'
        }

        for symbol in s:
            if symbol in '({[':
                stack.append(symbol)
            else:
                if len(stack)!=0:
                    if stack.pop() != parentheses[symbol]:
                        return False
                else:
                    return False

        return stack == []

print(Solution().isValid('()'))
print(Solution().isValid('()[]{}'))
print(Solution().isValid('(]'))
print(Solution().isValid(''))
print(Solution().isValid('()]'))
print(Solution().isValid('[(()]'))