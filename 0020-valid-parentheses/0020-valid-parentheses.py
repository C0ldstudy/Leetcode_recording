class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i in ['(', '[', '{']:
                stack.append(i)
            elif len(stack) == 0:
                return False
            elif (i == ')') and (stack[-1] == '('):
                stack.pop(-1)
            elif (i == ']') and (stack[-1] == '['):
                stack.pop(-1)
            elif (i == '}') and (stack[-1] == '{'):
                stack.pop(-1)            
            else:
                return False
        print(stack)
        if stack == []: return True
        return False

                
                
                