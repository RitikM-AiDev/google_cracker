from typing import List
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sum_ = sum(nums)
        t=0
        for i in range(len(nums)):
            t+=nums[i]
            sum_-=nums[i]
            if sum_ == t-nums[i]:
                return i
        return -1