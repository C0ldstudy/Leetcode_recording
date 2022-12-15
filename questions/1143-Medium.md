### 1143. Longest Common Subsequence

Given two strings `text1` and `text2`, return the length of their longest common subsequence. If there is no common subsequence, return `0`.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, `"ace"` is a subsequence of `"abcde"`.
A common subsequence of two strings is a subsequence that is common to both strings.

### Key idea
- Dynamic Programming:
  - Build an array
  - complete the first row
  - Design a equation to get new result based on the left one, the upper one or the left upper one.



### Solution
```python
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        length1 = len(text1)
        length2 = len(text2)
        if length1 == 0 or length2 == 0: return 0
        dp = [[None for x in range(length1)] for y in range(length2)]
        # dp = [[None]* length1 ]* length2
        for j in range(length1):
            if text2[0] in text1[:(j+1)]:
                dp[0][j] = 1
            else:
                dp[0][j] = 0
        for i in range(1, length2):
            for j in range(length1):
                if j == 0:
                    if text1[j] in text2[:(i+1)]:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = 0
                else:

                    if text1[j] == text2[i]:
                        dp[i][j] = dp[i-1][j-1]+1
                    else:
                        dp[i][j] = max(dp[i][j-1], dp[i-1][j])
        print(dp)
        return dp[length2-1][length1-1]
```
