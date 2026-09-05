class Solution:
    def twoSum(self, l: List[int], k: int) -> List[int]:
            i=0
            j=len(l)-1
            f=0
            while i<j:
                if l[i]+l[j] == k:
                    f=1
                    return [i+1,j+1]
                elif l[i]+l[j] < k:
                    i+=1
                else:
                    j-=1
            if f==0:
                return []
                    