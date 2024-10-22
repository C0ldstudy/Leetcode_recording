class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            # print(stack)
            if c in ['(', '[', '{']:
                stack.append(c)
            elif len(stack) == 0:
                return False
            else:
                temp = stack.pop(-1)
                if (c == ')') and (temp == '('):
                    continue
                elif (c == ']') and (temp == '['):
                    continue
                elif (c == '}') and (temp == '{'):
                    continue                   
                else:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False
    
            
                