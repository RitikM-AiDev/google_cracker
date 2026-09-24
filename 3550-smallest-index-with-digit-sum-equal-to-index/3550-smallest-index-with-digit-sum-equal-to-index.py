class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            n = nums[i]
            r=0
            while n>0:
                t = n%10
                r+=t
                n = n//10
            if r==i:
                return i
        return -1