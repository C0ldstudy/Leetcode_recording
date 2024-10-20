class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        num = list(num)
        # if len(num) == 1:
        #     if num[0] in ['1','8', '0']:
        #         return True
        #     else:
        #         return False
            
        if ('3' in num) or ('4' in num) or  ('7' in num) or ('2' in num) or ('5' in num):
            return False
        length = len(num) // 2
        for i in range(length):
            if num[i] == '0' and num[-i-1]=='0':
                continue
            if num[i] == '1' and num[-i-1]=='1':
                continue
             
            elif num[i] == '6' and num[-i-1]=='9':
                continue                
            elif num[i] == '9' and num[-i-1]=='6':
                continue
            elif num[i] == '8' and num[-i-1]=='8':
                continue
            else:
                return False
        # print(num)
        if len(num) % 2 != 0:
            if num[(len(num)//2)] in ['1', '8', '0']:
                return True
            else:
                return False
        else:
            return True