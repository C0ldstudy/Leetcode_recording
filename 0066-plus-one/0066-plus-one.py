class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] != 9:
            digits[-1] += 1
            return digits
        else:
            cnt = -1
            while digits[cnt] == 9:
                digits[cnt] = 0
                cnt -= 1
                if (len(digits) + cnt) == -1:
                    digits = [1] + digits
                    return digits
            digits[cnt] += 1
            return digits