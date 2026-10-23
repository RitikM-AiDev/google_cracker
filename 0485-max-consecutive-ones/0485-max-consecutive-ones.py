class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        c=0
        max_= 0
        for i in range(len(nums)):
            if nums[i]==1:
                c+=1
            else:
                max_ = max(max_,c)
                c=0
        max_ = max(max_,c)
        return max_