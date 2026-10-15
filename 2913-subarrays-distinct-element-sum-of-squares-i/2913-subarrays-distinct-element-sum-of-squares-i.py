class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        n=len(nums)
        sum_=0
        for i in range(n):
            s=[]
            for j in range(i,n):
                s.extend([nums[j]])
                sum_ += (len(set(s.copy())))**2
        return sum_
        
                