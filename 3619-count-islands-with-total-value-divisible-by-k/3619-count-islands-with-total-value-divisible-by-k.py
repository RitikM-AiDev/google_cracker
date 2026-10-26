class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        ans=0
        sol = [[0] * len(grid[0]) for _ in range(len(grid))]
        def bt(i,j,sol):
            if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or sol[i][j]==1:
                return 0
            if grid[i][j]==0:
                return 0
            sol[i][j]=1
            total = grid[i][j]
            total+=bt(i+1,j,sol)
            total+=bt(i,j+1,sol)
            total+=bt(i-1,j,sol)
            total+=bt(i,j-1,sol)
            return total
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]>0 and sol[i][j]==0:
                   island_sum =  bt(i,j,sol)
                   if island_sum%k==0:
                        ans+=1
        return ans
                
