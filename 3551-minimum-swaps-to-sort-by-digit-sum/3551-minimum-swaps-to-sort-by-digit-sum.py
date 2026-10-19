class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            nums[i] = (nums[i],i)
        temp = nums.copy()
        nums.sort(key=lambda x : (sum([int(i) for i in str(x[0])]),x[0]))
        visit=[False]*len(nums)
        c=0
        for i in range(len(nums)):
            start=i
            cycle=[]
            if visit[i]:
                continue
            while not visit[start]:
                visit[start]=True
                cycle.append(nums[start])
                start = nums[start][1]
            c+=(len(cycle)-1) 
        return c

            

