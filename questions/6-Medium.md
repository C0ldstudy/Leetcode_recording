### 6. Zigzag Conversion

The string `"PAYPALISHIRING"` is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

```
P   A   H   N
A P L S I I G
Y   I   R
```

And then read line by line: `"PAHNAPLSIIGYIR"`
Write the code that will take a string and make this conversion given a number of rows:
string convert(string s, int numRows);

### Key idea
- Find the equations to show the patterns of each line: for `i+k` line, the gap of index should be `i+2n-2k-3` and `2i`.




### Solution
```python
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: return s
        length = len(s)
        result = ''
        cur = 0
        while cur < length:
            result += s[cur]
            cur = cur + 2*numRows-2

        for i in range(1, numRows-1):
            cur = i
            while cur < length:
                result += s[cur]
                cur = cur + 2 * numRows - 2 * i - 3 + 1
                if cur < length:
                    result += s[cur]
                    cur = cur + 2*i
        cur = numRows-1
        while cur < length:
            result += s[cur]
            cur = cur + 2*numRows-2
        return result
```
