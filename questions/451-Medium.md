### 451. Sort Characters By Frequency
Given a string `s`, sort it in **decreasing order** based on the **frequency** of the characters. The **frequency** of a character is the number of times it appears in the string.
Return the sorted string. If there are multiple answers, return any of them.



### Key idea:
utilize counter class and sorted(list, key, reverse) function to count the characters and display them as the requirements.

### Solutions
```python
class Solution:
    def frequencySort(self, s: str) -> str:
        cnt = Counter(s)
        result = ''
        for k, v in sorted(cnt.items(), key=lambda item: item[1], reverse=True):
            result += k*v
        return result
```
