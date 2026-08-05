from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_= 0
        min_=float('inf')
        for i in prices:
            if i < min_:
                min_=i
            max_ = max(max_,i-min_)
        return max_

            