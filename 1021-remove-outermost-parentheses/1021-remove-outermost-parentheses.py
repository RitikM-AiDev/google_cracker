class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        st=[]
        r=""
        for i in range(len(s)):
            if s[i]=='(':
                if not st:
                    st.append(s[i])
                else:
                    st.append(s[i])
                    r+=s[i]
            else:
                if st and st[-1]=='(':
                    st.pop()
                    if not st:
                        continue
                    else:
                        r+=s[i]
        return r
       