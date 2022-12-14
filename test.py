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

