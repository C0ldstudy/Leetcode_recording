class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        seconds = 0
        for i in range(len(points)-1):
            dis = [abs(points[i+1][0] - points[i][0]), abs(points[i+1][1] - points[i][1])]
            sec = max(dis[0], dis[1])
            seconds += sec
        return seconds
        