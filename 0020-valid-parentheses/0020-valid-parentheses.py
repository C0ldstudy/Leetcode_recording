class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0: return True
        stack = deque([])
        for c in s:
            # print(stack)
            if (len(stack) == 0) and (c not in ['(', '[', '{']):
                return False
            elif len(stack) == 0 or (c in ['(', '[', '{']):
                stack.append(c)
            else:
                temp = stack.pop()
                if (c == ')') and (temp !='('):
                    return False
                if (c == ']') and (temp !='['):
                    return False                
                if (c == '}') and (temp !='{'):
                    return False 
        
        if len(stack) == 0: return True
        return False
                    
        