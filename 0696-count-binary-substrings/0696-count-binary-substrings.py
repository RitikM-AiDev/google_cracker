class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        c=0
        zero=0
        n=len(s)
        one=0
        prev=0
        for i in range(n):
            if s[i]=="0":
                zero+=1
            else:
                one+=1
            if i==n-1 or s[i] != s[i+1]:
                c+=min(prev,zero+one)
                prev = zero+one
                zero=0
                one=0
        return c