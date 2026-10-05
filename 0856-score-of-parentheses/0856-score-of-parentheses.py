class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        score=0
        st=[0]
        for i in s:
            if i=="(":
                st.append(0)
            else:
                inner = st.pop()
                if inner ==0 :
                    v = inner +1
                else:
                    v = 2*inner
                st[-1]+=v
        return st[-1]
                 
            