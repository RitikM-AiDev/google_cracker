class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        n=0
        nums.sort()
        mid=len(nums)//2
        for i in nums:
            n+=(abs(nums[mid]-i))
        return n