class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        res=0
        max_ = max(nums).bit_length()
        arr=[0]*max_
        for i in nums:
            bin_ = bin(i)[2:]
            for j in range(len(bin_)-1,-1,-1):
                if bin_[j]=='1':
                    arr[len(bin_)-1-j]+=1
        while k>0:
            s=""
            for i in range(len(arr)-1,-1,-1):
                if arr[i]>0:
                    arr[i]-=1
                    s+='1'
                else:
                    s+='0'
            res+=(int(s,2)**2)
            k-=1
        return res % ((10**9)+7)


        

