class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        min_=float('inf')
        sol = [[set() for _ in range(len(grid[0]))] for _ in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == 0 and j == 0:
                    sol[i][j].add(grid[i][j])
                elif i==0:
                    for k in sol[i][j-1]:
                        sol[i][j].add(k^grid[i][j])
                elif j==0:
                    for k in sol[i-1][j]:
                        sol[i][j].add(k^grid[i][j])
                else:
                    for k in sol[i-1][j]:
                        sol[i][j].add(k^grid[i][j])
                    for k in sol[i][j-1]:
                        sol[i][j].add(k^grid[i][j])
                    

        return min(sol[-1][-1])