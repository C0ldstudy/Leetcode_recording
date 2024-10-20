class Solution:
    def removeDuplicates(self, s: str) -> str:
        output = []
        for c in s:
            if output and c == output[-1]:
                output.pop(-1)
            else:
                output.append(c)
        return ''.join(output)