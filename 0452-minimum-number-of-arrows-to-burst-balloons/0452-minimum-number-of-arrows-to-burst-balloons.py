class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points = sorted(points, key = lambda x: (x[0], x[1]))
        length = len(points)
        result = 1
        for i in range(1, length):
            if points[i][0] > points[i-1][1]:
                result += 1
            else:
                points[i][1] = min(points[i][1], points[i-1][1])
        return result
            