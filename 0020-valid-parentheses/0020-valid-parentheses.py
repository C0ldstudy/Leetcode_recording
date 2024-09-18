class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i in ['(', '[', '{']:
                stack.append(i)
            else:
                if stack == []: return False
                if (stack[-1] == '(') and (i==')'):
                    stack.pop()
                elif (stack[-1] == '[') and (i==']'):
                    stack.pop()
                elif (stack[-1] == '{') and (i=='}'):
                    stack.pop()
                else:
                    return False
        if stack == []:
            return True
        else:
            return False
                
        