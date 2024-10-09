class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        for i in s:
            if i == ')':
                if len(stack) != 0:
                    if stack[-1] == '(':
                        stack.pop(-1)
                    else:
                        stack.append(i)
                else:
                    stack.append(i)
            else:
                stack.append(i)
        return len(stack)
                