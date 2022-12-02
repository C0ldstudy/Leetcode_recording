### 1657. Determine if Two Strings Are Close

Two strings need to be decided that they are close if they can be the same after multiple times of the following two actions:
- Swap any two existing characters.
- Transform every occurrence of one existing character into another existing character, and do the same with the other character.

### Key ideas:
Two actions means:
- The order of the string can be changed totally.
- The frequency of each character can be swapped.

So if two strings have same unique characters and frequencies of all the characters are the same, they are close.


### Solution
```python
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        cnt1 = Counter(word1)
        cnt2 = Counter(word2)
        if cnt1.keys() != cnt2.keys():
            return False
        elif sorted(list(cnt1.values())) != sorted(list(cnt2.values())):
            return False
        else:
            return True
```
