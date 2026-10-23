class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        l = set(nums)
        arr=[]
        for i in range(1,len(nums)+1):
            if i not in l:
                arr.append(i)
        return arr

