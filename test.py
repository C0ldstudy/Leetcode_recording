from typing import List

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if (x <= arr[0]):
            return arr[:k]
        elif (x >= arr[-1]):
            return arr[-k:]
        else:
            new_arr = []
            for item in arr:
                new_arr.append(abs(item-x))
            # print(new_arr)
            index = self.argsort(new_arr)[:k]#.sort()
            index.sort()
            # print(index)

            result = []
            for i in index:
                result.append(arr[i])
            return result

    def argsort(self, seq):
    # http://stackoverflow.com/questions/3071415/efficient-method-to-calculate-the-rank-vector-of-a-list-in-python
        print(seq.__getitem__)

        return sorted(range(len(seq)), key=seq.__getitem__)



test = Solution()
test_input = [1,2,3,4,5]
k = 4
x = 3

print(test.findClosestElements(test_input, k, x))
