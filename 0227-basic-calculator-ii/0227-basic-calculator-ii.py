class Solution:
    def calculate(self, s: str) -> int:
        result = 0
        number = ''
        aux_num = ''
        prev_op = '+'
        s = ''.join(s.split(' '))
        
        for char in s + '+':
            if char.isdigit():
                number += char
            elif char in '-+':
                match prev_op:
                    case '+':
                        result += int(number)
                        number = ''
                    case '-':
                        result -= int(number)
                        number = ''
                    case '*':
                        result += int(number) * int(aux_num)
                        number, aux_num = '', ''
                    case '/':
                        result += int(int(aux_num) / int(number))
                        number, aux_num = '', ''
                prev_op = char
            elif char in '*/':
                match prev_op:
                    case '*':
                        aux_num = int(number) * int(aux_num)
                        number = ''
                    case '/':
                        aux_num = int(int(aux_num)/ int(number))
                        number = ''
                    case '+':
                        aux_num = number
                        number = ''
                    case '-':
                        aux_num = '-'+number
                        number = ''
                prev_op = char
        return result
                        
                        