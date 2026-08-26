class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res =[]
        t = {2: "abc", 3:"def", 4: "ghi", 5: "jkl" , 6 : "mno", 7: "pqrs", 8:  "tuv", 9: "wxyz"}
        def bt(i,sol):
            if len(sol) > len(digits) or i<0 or i>=len(digits)+1:
                return 
            if len(sol)==len(digits):
                m = "".join(sol)
                print(m)
                res.append(m)
                return 
            for k in t[int(digits[i])]:
                sol.append(k)
                bt(i+1,sol)
                sol.pop()
        bt(0,[])
        return res
            
    