class Solution:
    def countKDifference(self, nums: list[int], k: int) -> int:
        f={}
        c=0
        for i in range(len(nums)):
            rem1 = nums[i]+k
            rem2 = nums[i]-k
            if rem1 in f:
                for j in f[rem1]:
                    c+=1
            if rem2 in f:
                for j in f[rem2]:
                    c+=1
            f[nums[i]] = f.get(nums[i],[])
            f[nums[i]].append(i)
        return c

            
            


