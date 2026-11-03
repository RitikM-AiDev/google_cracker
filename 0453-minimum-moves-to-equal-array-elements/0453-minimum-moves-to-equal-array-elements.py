class Solution:
    def minMoves(self, nums: list[int]) -> int:
        if len(set(nums)) == 1:
            return 0
        nums.sort()
        n=0
        min_=min(nums)
        for i in nums:
            n+=(abs(min_-i))
        return n