class Solution:
    def minOperations(self, nums: List[int]) -> int:
        if sorted(nums)==nums:
            return 0
        rev = nums[::-1]
        r = rev + rev
        k3 = -1
        for i in range(len(rev)):
            if r[i] == len(rev) - 1:
                s = i
                f = 0
                c = 0

                while c < len(rev):
                    if r[s + c] != len(rev) - 1 - c:
                        f = 1
                        break
                    c += 1

                if f == 0:
                    k3 = s + 2
                    break
        r=nums+nums
    
        k=-1
        for i in range(len(nums)):
            if r[i]==0:
                s=i
                f=0
                c=0
                while c<len(nums):
                    if r[c+s] !=c:
                        f=1
                        break
                    c+=1
                if f==0:
                    k = s
                    break
        k2=-1
        for i in range(len(nums)-1,-1,-1):
            if r[i]==len(nums)-1:
                s=i
                f=0
                c=0
                while c<len(nums):
                    if r[s+c] !=len(nums)-c-1:
                        f=1
                        break
                    c+=1
                if f==0:
                    k2 = s+1
                    break
        nums = nums[::-1]
        r = nums+nums
    
        k1=-1
        for i in range(len(nums)):
            if r[i]==0:
                s=i
                f=0
                c=0
                while c<len(nums):
                    if r[c+s] !=c:
                        f=1
                        break
                    c+=1
                if f==0:
                    k1 = s+1
                    break
        nums = nums[::-1]
        valid=[]
        for i in (k1,k2,k,k3):
            if i!=-1:
                valid.append(i)
        return min(valid) if valid else -1
                    