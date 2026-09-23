class Solution:
    def replaceDigits(self, s: str) -> str:
        r = ""
        for i in range(len(s)):
            if i%2==0:
                r+=s[i]
            else:
                shift = ord(s[i-1]) + int(s[i])
                r+=chr(shift) 
        return r
