class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        intervals.append(newInterval)
        intervals.sort(key=lambda x: x[0])

        res = []
        for i in intervals:
            if res and i[0] <= res[-1][1]:
                point = [res[-1][0], max(res[-1][1], i[1])]
                res[-1] = point
            else:
                res.append(i)

        return res