class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        for i in range(n,n+11):
            p=1
            l=i
            while i>0:
                r = i%10
                p*=r
                i//=10
            if p%t==0:
                return l
            