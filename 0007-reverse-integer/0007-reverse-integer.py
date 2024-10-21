class Solution:
    def reverse(self, x: int) -> int:
        if (x < -2**31) or (x > (2**31-1)):
            return 0
        
        if x < 0:
            sign = -1
            num = list(str(x)[1:])
        else:
            sign = 1
            num = list(str(x)[:])
        
        num.reverse()
        if sign == -1:
            result = -1 * int(''.join(num))
        else:
            result =  int(''.join(num))
        if (result < -2**31) or (result > (2**31-1)):
            return 0
        else:
            return result