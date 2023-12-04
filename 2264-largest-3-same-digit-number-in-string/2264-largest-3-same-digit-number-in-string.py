class Solution:
    def largestGoodInteger(self, num: str) -> str:
        # for i in range(len(num)):
        i = 0
        result = []
        
        while i < len(num):
            j = 1
            while i+j < len(num):
                if num[i+j] == num[i]: 
                    j += 1
                else:
                    # print(j)
                    if j >= 3:
                        result.append(int(num[i]))
                    # result.apend(j)
                    break
            i = i+j
        if j >= 3: result.append(int(num[i-1]))
        # print(result)
        if len(result) == 0: return ''
        return str(max(result))*3
        
        