class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] != 9:
            digits[-1] += 1
            return digits
        
        for i in range(len(digits)-1,-1,-1):
            flag=0
            if digits[i] == 9:
                digits[i] = 0
                flag = 1
            else:
                digits[i] += 1
                break
        if flag == 0:
            return digits
        else:
            digits = [1] + digits
            return digits