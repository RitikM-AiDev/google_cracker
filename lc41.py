from typing import List
class Solution:
   def firstMissingPositive(self, nums: List[int]) -> int:
        s_=1
        nums.sort()
        for i in nums:
            if i>0:
                if i==s_:
                    s_+=1
        return s_
    