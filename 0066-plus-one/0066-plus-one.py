class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] != 9: 
            digits[-1] += 1
            return digits
        else:
            digits[-1] = 0
            i = -2
            while i >= -len(digits):
                # print(digits)
                if digits[i] == 9:
                    digits[i] = 0
                    i -= 1
                else:
                    digits[i] += 1
                    break
            # print(i)
            if i < -len(digits):
                digits = [1] + digits
                return digits
            else:
                return digits
                