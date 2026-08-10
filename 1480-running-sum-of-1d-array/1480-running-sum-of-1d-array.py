class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        l=[0]*len(nums)
        l[0]=nums[0]
        t = nums[0]
        for i in range(1,len(nums)):
                t+=nums[i]
                l[i] = t
        l[-1]=t
        return l