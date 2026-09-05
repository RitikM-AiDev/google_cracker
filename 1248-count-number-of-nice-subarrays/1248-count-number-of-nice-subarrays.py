class Solution:
    def numberOfSubarrays(self, l: List[int], k: int) -> int:
        ans=0
        dp=[0]*len(l)
        for i in range(len(l)):
            if l[i]%2!=0:
                l[i] =1
            else:
                l[i]=0
        dp[0]=l[0]
        f={0:1}
        count=0
        for i in range(1,len(l)):
            dp[i] = dp[i-1]+l[i]
        for i in range(len(l)):
            f[dp[i]] = f.get(dp[i],0)+1
            if dp[i]- k in f:
                count+=f.get(dp[i]-k,0)
        return count