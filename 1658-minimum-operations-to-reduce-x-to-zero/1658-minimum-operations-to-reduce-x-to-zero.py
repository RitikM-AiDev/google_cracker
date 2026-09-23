class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        l = nums
        n = len(nums)
        pre1 = [0]*(n+1)
        pre2 = [0]*(n+1)
        f={}
        min_= float('inf')
        for i in range(1,n+1):
            pre1[i] = pre1[i-1] + l[i-1]
        for i in range(n-1,-1,-1):
            pre2[n-i] = pre2[n-i-1] + l[i]
        for i in range(len(pre2)):
            f[pre2[i]] = f.get(pre2[i],i)
        print(f)
        for i in range(len(pre1)):
            rem = x - pre1[i]
            if rem in f:
                if (f[rem] + i)< min_ and i+f[rem]<=n:
                    min_ = f[rem]+i
        if min_ == float('inf'):
            return -1
        else:
            return min_

