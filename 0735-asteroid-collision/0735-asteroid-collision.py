class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        left = []
        for a in asteroids:
            # print(a, left, stack)
            if (a < 0) and (len(stack) == 0):
                left.append(a)
                continue
            elif len(stack) == 0:
                stack.append(a)
            else:
                if stack[-1] * a > 0:
                    stack.append(a)
                else:
                    if abs(stack[-1]) == abs(a):
                        stack.pop(-1)
                        continue                    
                    # if len(stack) == 0:
                    #     break  
                    while abs(stack[-1]) <= abs(a):
                        if abs(stack[-1]) == abs(a):
                            stack.pop(-1)
                            break
                        else:
                            stack.pop(-1)
                            if len(stack) == 0:
                                left.append(a)
                                break
        # print(left, stack)
        return left+stack
                    
                        
                        