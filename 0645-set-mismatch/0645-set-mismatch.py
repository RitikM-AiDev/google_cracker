class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        f={}
        l=[]
        sum_=0
        n=len(nums)
        for i in nums:
            f[i] = f.get(i,0)+1
        for k,v in f.items():
            if v>1:
                l.append(k)
            sum_+=k
        if 1 not in f:
            l.append(1)
        else:
            l.append(((n * (n+1))//2) - sum_)
        return l
              