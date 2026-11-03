class Solution:
    def minMoves(self, nums: List[int]) -> int:
        n=0
        max_=max(nums)
        for i in nums:
            n+=(max_-i)
        return n