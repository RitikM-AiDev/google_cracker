class Solution:
    def shiftingLetters(self, s: str, shifts: list[int]) -> str:
        for i in range(len(s)-2,-1,-1):
            shifts[i] = shifts[i]+shifts[i+1]
        print(shifts)
        r=""
        for i in range(len(s)):
            res =ord(s[i]) + (shifts[i] %26)
            if  res > ord('z'):
                    res -=26
            r+=chr(res)   
        return r