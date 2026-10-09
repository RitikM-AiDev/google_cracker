class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        res=[]
        nums.sort()
        def bt(start,sol):
            nonlocal res
            res.append(sol.copy())
            if start==len(nums):
                return
            for j in range(start,len(nums)):
                if start < j and  nums[j-1]==nums[j]:
                    continue
                sol.append(nums[j])
                bt(j+1,sol)
                sol.pop()
        bt(0,[])
        return res

