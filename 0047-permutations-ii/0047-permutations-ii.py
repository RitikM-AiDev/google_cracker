class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res= []
        nums.sort()
        visited = [False]*len(nums)
        def bt(sol):
            if len(sol) == len(nums):
                res.append(sol.copy())
                return 
            for j in range(len(nums)):
                if j>0 and  nums[j]==nums[j-1] and not visited[j-1]:
                    continue
                if not visited[j]:
                        sol.append(nums[j])
                        visited[j] = True
                        bt(sol)
                        sol.pop()
                        visited[j] = False
        bt([])
        return res
                    
                

        
