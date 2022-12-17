### 150. Evaluate Reverse Polish Notation


Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are **+, -, *, and /**. Each operand may be an integer or another expression.

Note that division between two integers should truncate toward zero.

It is guaranteed that the given RPN expression is always valid. That means the expression would always evaluate to a result, and there will not be any division by zero operation.


### Key idea:
- I just use a recursive method to get the answer.
- A better way is to use lambda and stack. Check Algorithm 2.

### Solution
```python
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operation = ['+', '-', '*', '/']
        if len(tokens) == 1: return int(tokens[0])
        def operate(num1, num2, op):
            num1, num2 = int(num1), int(num2)
            if op == '+':
                return num1 + num2
            elif op == '-':
                return num1 - num2
            elif op == '*':
                return num1 * num2
            elif op == '/':
                return num1 / num2
        def execute(string_list):
            if len(string_list) == 1: return string_list[0]

            for i, item in enumerate(string_list):
                if item in operation:
                    string_list = string_list[:(i-2)] + [operate(string_list[i-2], string_list[i-1], string_list[i])] + string_list[(i+1):]
                    break
            string_list = execute(string_list)
            return string_list
        result = execute(tokens)
        return int(result)
```

```python
class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        operations = {
            "*": lambda x,y: x*y,
            "+": lambda x,y: x+y,
            "-": lambda x,y: x-y,
            "/": lambda x,y: float(x)/y
        }

        stack = []
        for token in tokens:
            if token not in operations:
                stack.append(int(token))
            else:
                right = stack.pop()
                left = stack.pop()
                result = operations[token](left, right)
                stack.append(int(result))
        return stack.pop()
```
