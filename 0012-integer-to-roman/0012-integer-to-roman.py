class Solution:
    def intToRoman(self, num: int) -> str:
        number_list = [1000, None, 100, None, 10, None, 1]
        symbol_list = ['M', 'D', 'C', 'L', 'X', 'V', 'I']
        result = ''
        for i, number in enumerate(number_list):
            if number == None:
                continue
            integer = int(num/number)            
            if integer == 0:
                continue
            elif integer == 4:
                result += symbol_list[i] + symbol_list[i-1]
                num = num - integer * number
                # num
                continue
            elif integer == 9:
                result += symbol_list[i] + symbol_list[i-2]
                num = num - integer * number
                continue   
            elif integer == 5:
                result += symbol_list[i-1]
                num = num - integer * number
                continue                 
            elif integer >5:
                result += symbol_list[i-1] + symbol_list[i]*(integer-5)
                num = num - integer * number                
                continue
            result += symbol_list[i] * integer
            num = num - integer * number
        return result
            
            
            
            
        