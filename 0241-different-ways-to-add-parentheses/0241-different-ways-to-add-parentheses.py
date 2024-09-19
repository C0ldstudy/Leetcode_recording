class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        result = []
        
        eq = expression#.split("+").split("-").split("*")
        if len(eq) == 0: return result
        if len(eq) == 1:
            return [int(eq)]
        if (len(eq) == 2) and (eq[0].isdigit()):
            return [int(eq)]
        
        
        for i, n in enumerate(eq):
            if n.isdigit(): continue
            left_result = self.diffWaysToCompute(expression[:i])
            right_result = self.diffWaysToCompute(expression[i+1:])
                
            for left in left_result:
                for right in right_result:
                    if n == "+":
                        result.append(left + right)
                    elif n == "-":
                        result.append(left - right)
                    elif n == "*":
                        result.append(left * right)
        
        return result
                
        
        
                
    