class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        res = []
        if len(expression) == 0: 
            return []
        elif (len(expression) <= 2 and expression.isdigit()):
            return [int(expression)]
        
        for i, e in enumerate(expression):
            if e.isdigit(): continue
            left_res = self.diffWaysToCompute(expression[:i])
            right_res = self.diffWaysToCompute(expression[i+1:])
            for left in left_res:
                for right in right_res:
                    if e == "+":
                        res.append(left+right)
                    if e == "-":
                        res.append(left-right)                
                    if e == "*":
                        res.append(left*right)
        return res
        