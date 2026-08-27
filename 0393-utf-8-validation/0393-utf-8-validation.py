class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        res=[]
        for i in data:
            b = bin(i)[2:].zfill(8).split('0')
            print(bin(i)[2:])
            c = b[0].count('1')
            res.append(c)
        i=0
        while i<len(res):
            if res[i]==0:
                i+=1
            elif res[i]==2:
                if i+1 < len(res) and res[i+1] == 1:
                    i+=2
                else:
                    return False
            elif res[i] ==3:
                if i+ 2< len(res) and res[i+1]==res[i+2] ==1:
                    i+=3
                else:
                    return False
            elif res[i]==4:
                if i+3 < len(res) and res[i+1]==res[i+2]==res[i+3]==1:
                    i+=4 
                else:
                    return False
            else:
                return False
        return True

                
                   
            
