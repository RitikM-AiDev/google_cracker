from typing import List
class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        l = sorted(nums,reverse=True)
        res=[]
        v=l.pop()
        while l:
            v+=1
            if v==l[-1]:
                l.pop()
            else:
                res.append(v)
        return res
    