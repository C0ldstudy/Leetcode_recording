class Solution:
    def compressedString(self, word: str) -> str:
        stack = []
        result = ''
        for c in word:
            if len(stack) == 0:
                stack.append(c)
            elif c == stack[-1] and len(stack) != 9:
                stack.append(c)
            elif len(stack) == 9 or c != stack[-1]:
                result += str(len(stack)) + stack[-1]
                stack = []
                stack.append(c)
        result += str(len(stack)) + stack[-1]

            # print(stack)
        return result