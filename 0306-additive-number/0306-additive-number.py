class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        def bt(i,sol):
            if i==len(num):
                if len(sol) < 3:
                    return False
                for k in range(2,len(sol)):
                    if sol[k] != sol[k-1]+sol[k-2]:
                        return False
                return True
            for j in range(i,len(num)):
                curr = num[i:j+1]
                if len(curr)>1 and curr[0]=='0':
                    break
                if len(sol)>=2 and sol[-1]+sol[-2]<int(curr):
                    break
                sol.append(int(curr))
                if bt(j+1,sol):
                    return True
                sol.pop()
            return False
        return bt(0,[])
