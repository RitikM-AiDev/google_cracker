class Solution:
    def grayCode(self, n: int) -> List[int]:
        res = [0]
        for i in range(n):
            j = 2**i
            for k in range(len(res)-1,-1,-1):
                res.append(j+res[k])
        return res
