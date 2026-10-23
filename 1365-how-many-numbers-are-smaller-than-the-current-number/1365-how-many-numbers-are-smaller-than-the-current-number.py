class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        arr=[]
        for i in range(len(nums)):
            c=0
            for j in range(len(nums)):
                if i!=j:
                    if nums[j] < nums[i]:
                        c+=1
            arr.append(c)
        return arr