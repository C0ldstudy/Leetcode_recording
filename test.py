from typing import List, Optional
class Solution:
    def trap(self, height: List[int]) -> int:
        temp = []
        current = 0

        for i, h in enumerate(height):
            if (h >= current) & (h != 0):
                temp.append([i, h])
                current = h
            elif h < current:
                flag = 0
                for j in height[i+1:]:
                    # print('inn: ', i, h, j)
                    if h <= j:
                        flag = 1
                        break

                if flag == 0:
                    temp.append([i, h])
        # print(temp)
        # calculate the areas
        whole_area = 0
        for i in range(len(temp)-1):
            area = min(temp[i][1], temp[i+1][1]) * (temp[i+1][0] - temp[i][0]-1)
            rock_area = 0
            # print("range", temp[i][0]+1, temp[i+1][0])
            for j in range(temp[i][0]+1, temp[i+1][0]):
                rock_area += height[j]
            whole_area = whole_area + area - rock_area
            # print(area, rock_area)
        return whole_area


height = [0,1,0,2,1,0,1,3,2,1,2,1,1]
test = Solution()
print(test.trap(height))

