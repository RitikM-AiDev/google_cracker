class Solution:
    def compress(self, chars: list[str]) -> int:
        curr = 1
        j=0
        n = len(chars)
        for i in range(n-1):
            if chars[i] == chars[i+1]:
                    curr+=1
            else:
                chars[j] = chars[i]
                j+=1
                if curr > 1:
                    curr = str(curr)
                    for num in curr:
                        chars[j] = num
                        j+=1
                    curr=1
        chars[j] = chars[-1]
        j+=1
        if curr > 1:
            curr = str(curr)
            for num in curr:
                chars[j] = num
                j+=1
            curr=1
        curr=n-1
        while curr > j-1:
            if chars:
                chars.pop()
                curr-=1
