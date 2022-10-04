### 1578. Minimum Time to Make Rope Colorful
Alice has n balloons arranged on a rope. You are given a 0-indexed string colors where colors[i] is the color of the ith balloon.

Alice wants the rope to be colorful. She does not want two consecutive balloons to be of the same color, so she asks Bob for help. Bob can remove some balloons from the rope to make it colorful. You are given a 0-indexed integer array neededTime where neededTime[i] is the time (in seconds) that Bob needs to remove the ith balloon from the rope.

Return the minimum time Bob needs to make the rope colorful.


### Key idea
- Get the indexes of these repeated items.
- Get the cost by summing them all and reducing the largest one.


### Solution
```python
from typing import List, Optional
class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        repeated_items = []
        current = 0
        while current < (len(colors)-1):
            i = 1
            # print(current, i)
            while colors[current + i] == colors[current]:
                i += 1
                if current + i == len(colors):
                    break
            if i > 1:
                repeated_items.append([current, (current+i-1)])
            current = current + i
            # print(repeated_items)
        result = 0
        for i in repeated_items:
            temp = []
            for j in range(i[0], i[1]+1):
                temp.append(neededTime[j])

            # print(temp)
            result = result + sum(temp) - max(temp)
        return result

colors = "bbbaaa"
neededTime = [4,9,3,8,8,9]
test = Solution()
print(test.minCost(colors, neededTime))
```
