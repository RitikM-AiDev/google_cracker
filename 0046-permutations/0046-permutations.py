class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        visited=[False]*(len(nums))
        ans=[]
        def bt(i,sol):
            nonlocal ans,visited
            if i==len(nums):
                ans.append(sol.copy())
                return
            for j in range(len(nums)):
                if not visited[j]:
                    sol.append(nums[j])
                    visited[j]=True
                    bt(i+1,sol)
                    sol.pop()
                    visited[j]=False
        bt(0,[])
        return ans