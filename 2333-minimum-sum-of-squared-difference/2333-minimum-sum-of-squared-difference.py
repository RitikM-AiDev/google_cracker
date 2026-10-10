class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        arr=[abs(nums1[i]-nums2[i]) for i in range(len(nums1))]
        k = k1+k2
        l=0
        h = max(arr)
        if sum(arr)<=k:
            return 0
        while l<h:
            mid = (l + h)//2
            n = sum([max(0,i-mid) for i in arr])
            if n>k:
                l = mid+1
            else:
                h=mid
        m=l
        n = sum([max(0,i-m) for i in arr])
        rem = k-n
        for i in range(len(arr)):
            if arr[i]>m:
                arr[i]=m
        i=0
        while rem>0 and i<len(arr):
            if arr[i]==m:
                arr[i]-=1
                rem-=1
            i+=1
        return sum([i**2 for i in arr])                
            


