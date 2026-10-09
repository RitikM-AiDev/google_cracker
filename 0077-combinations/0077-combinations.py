class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        visited=[False]*n
        arr=[]
        res=[]
        for i in range(1,n+1):
            arr.append(i)
        def bt(j,sol):
            if len(sol)==k:
                res.append(sol.copy())
                return
            for j in range(j,n):
                if not visited[j]:
                    sol.append(arr[j])
                    visited[j]=True
                    bt(j+1,sol)
                    sol.pop()
                    visited[j]=False
        bt(0,[])
        return res
