class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        i=0
        j=len(height)-1
        left_max=right_max=0
        while i<=j:
            if height[i] < height[j]:
                if height[i] >= left_max:
                    left_max = max(height[i],left_max)
                else:
                    water+=left_max - height[i]
                i+=1
            else:
                if height[j] >= right_max:
                    right_max = max(height[j],right_max)
                else:
                    water+=right_max - height[j]
                j-=1
        
        return water

            
