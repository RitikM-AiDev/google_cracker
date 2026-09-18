class Solution:
    def canPartition(self, nums: list[int]) -> bool:
            nums.sort()
            l = nums
            if sum(nums)%2!=0:
                return False
            t= sum(nums)//2
            n=len(nums)
            dp = [[None]*(t+1) for _ in range(n)]
            for i in range(n):
                for j in range(t+1):
                    if j==0:
                        dp[i][j]=True
                    elif i==0:
                        if l[i]==j:
                            dp[i][j]=True
                        else:
                            dp[i][j]=False
                    else:
                        if j < l[i]:
                            dp[i][j] = dp[i-1][j]
                        else:
                            dp[i][j] = dp[i-1][j] |dp[i-1][j-l[i]]
            return dp[-1][t]

            