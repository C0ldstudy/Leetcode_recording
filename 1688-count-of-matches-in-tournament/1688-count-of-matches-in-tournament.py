class Solution:
    def numberOfMatches(self, n: int) -> int:
        sum = 0
        while n > 1:
            sum += int(n/2)
            if n % 2 == 0:
                n = n/2
            else:
                n = int(n/2) + 1
        return sum

            