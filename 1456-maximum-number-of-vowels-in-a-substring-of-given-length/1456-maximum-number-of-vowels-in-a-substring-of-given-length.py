class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        t = s[:k]
        vow=('a','e','i','o','u')
        v=0
        for i in t:
            if i in vow:
                v+=1
        j=0
        max_=v
        for i in range(k,len(s)):
            if s[j] in vow:
                v-=1
            j+=1
            if s[i] in vow:
                v+=1
            max_ = max(v,max_)
        return max_
            
