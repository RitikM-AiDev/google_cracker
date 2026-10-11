class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        arr=[]
        res = []
        for i in range(1,9+1):
            arr.append(i)
        def bt(i,sol):
            nonlocal res
            if sum(sol)>n:
                return
            if len(sol)==k:
                print(sol)
                if sum(sol)==n:
                    res.append(sol.copy())
                return 
            if i<0 or i>=len(arr):
                return
            sol.append(arr[i])
            bt(i+1,sol)
            sol.pop()
            bt(i+1,sol)
        bt(0,[])
        return res