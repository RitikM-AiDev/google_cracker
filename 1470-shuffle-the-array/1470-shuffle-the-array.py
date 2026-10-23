class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        arr=[]
        n = len(nums)
        for i in range(n//2):
            arr.append(nums[i])
            arr.append(nums[i+n//2])
        return arr