class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        if sorted(nums)==nums:
            return 0
        for i in range(len(nums)):
            if i!=nums[i]:
                r=nums[i]
                break
            else:
                continue
        for i in range(len(nums)):
            if nums[i] !=i:
                r = r &i
        return r