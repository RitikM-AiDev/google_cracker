class Solution:
    def minInsertions(self, s: str) -> int:
        i=0
        st=[]
        c=0
        while i<len(s):
            if s[i]=='(':
                st.append(s[i])
                i+=1
            else:
                if st and st[-1]=='(':
                    if i+1<len(s) and s[i] == s[i+1]==')':
                        st.pop()
                        i+=2
                    else:
                        st.pop()
                        c+=1
                        i+=1
                else:
                    if i+1<len(s) and s[i]==s[i+1]==')':
                        c+=1
                        i+=2
                    else:
                        c+=2
                        i+=1
        c+=len(st)*2
        return c