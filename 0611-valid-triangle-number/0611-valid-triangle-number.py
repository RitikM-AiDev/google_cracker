class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        i=0
        n=len(nums)
        c=0
        k=n-1
        while k>=0:
            i=0
            j=k-1
            while i<j:
                if nums[i]+nums[j]<=nums[k]:
                    i+=1
                else:
                    c+=(j-i)
                    j-=1
            k-=1
        return c

