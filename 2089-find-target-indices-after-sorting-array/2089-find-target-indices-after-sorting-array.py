class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        nums.sort()
        l=[]
        for i,v in enumerate(nums):
            if v==target:
                l.append(i)
        return l