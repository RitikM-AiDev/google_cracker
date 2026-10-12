class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        res=[]
        intervals.sort(key=lambda x: x[0])
        for i in range(len(intervals)):
                if res and intervals[i][0] <= res[-1][-1]:
                    point = [min(intervals[i][0],res[-1][0]),max(intervals[i][-1],res[-1][-1])]
                    res[-1]=point
                else:
                    res.append(intervals[i])
        return res
