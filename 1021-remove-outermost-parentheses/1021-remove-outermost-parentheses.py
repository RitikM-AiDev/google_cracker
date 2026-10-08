class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        st=[]
        c=0
        for i in s:
            if i=='(':
                if c>0:
                    st.append(i)
                c+=1
            else:
                c-=1
                if c>0:
                    st.append(i)
        return "".join(st)
