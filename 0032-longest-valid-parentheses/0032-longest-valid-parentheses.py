class Solution:
    def longestValidParentheses(self, s: str) -> int:
        max_=0
        st=[-1]
        for i in range(len(s)):
            if s[i]=='(':
                st.append(i)
            else:
                st.pop()
                if not st:
                    st.append(i)
                else:
                    length = i -st[-1]  
                    max_ = max(max_,length)
        return max_