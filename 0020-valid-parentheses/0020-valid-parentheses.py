class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for idx in range(len(s)):
            if s[idx] not in [')', ']', '}']:
                stack.append(s[idx])
            else:
                if len(stack) == 0: return False
                if s[idx] == '}' and stack[-1] == '{':
                    stack.pop(-1)
                elif s[idx] == ')' and stack[-1] == '(':
                    stack.pop(-1)
                elif s[idx] == ']' and stack[-1] == '[':
                    stack.pop(-1)                    
                else:
                    return False
        if len(stack) == 0: return True
        return False
        