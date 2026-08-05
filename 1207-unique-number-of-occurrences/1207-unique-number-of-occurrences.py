class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        f={}
        set_=set()
        for i in arr:
            f[i] = f.get(i,0)+1
        for k,v in f.items():
            set_.add(v)
        if len(set_)!=len(f):
            return False
        else:
            return True
            
        