class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        total=0
        sol=[[0]*len(grid[0]) for _ in range(len(grid))]
        def bt(i,j,sol):
            nonlocal total
            if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]):
                return False
            if i==0 or j==0 or i==len(grid)-1 or j==len(grid[0])-1:
                sol[i][j]=1
                if grid[i][j]==0:
                    return False
                else:
                    return True
            if sol[i][j]==1:
                return True
            if grid[i][j]==1:
                return True
            sol[i][j]=1
            res1 = bt(i+1,j,sol)
            res2 = bt(i,j+1,sol)
            res3 = bt(i-1,j,sol)
            res4 = bt(i,j-1,sol)
            return res1 and res2 and res3 and res4
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==0 and sol[i][j]==0:
                    if bt(i,j,sol):
                        total+=1
        return total
            

            