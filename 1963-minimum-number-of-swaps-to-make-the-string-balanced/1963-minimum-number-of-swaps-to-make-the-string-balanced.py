class Solution:
    def minSwaps(self, s: str) -> int:
        stack = []
        unbalance = 0
        for i in s:
            if i == '[':
                stack.append(i)
            else:
                if stack:
                    stack.pop()
                else:
                    unbalance += 1
        return (unbalance+1)//2