class Solution:
    def countAndSay(self, n: int) -> str:
        result = []
        result.append('1')
        for i in range(1, n):
            result.append(self.say(result[i-1]))
        # print(result)
        return result[n-1]
   
    def say(self, num):
        temp = ''
        cur = 0
        count = 1
        while cur < len(num):
            if cur == len(num)-1:
                temp += str(count)+str(num[cur])
                break
            if num[cur] == num[cur+1]:
                count += 1
                cur += 1
            else:
                temp += str(count)+str(num[cur])
                count = 1
                cur += 1
        # temp = 
        return str(temp)
            
            