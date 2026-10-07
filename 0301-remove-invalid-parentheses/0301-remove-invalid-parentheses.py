class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        ans= set()
        st=[]
        a=0
        b=0
        for i in s:
            if i=='(':
                st.append(i)
            elif i==')':
                if st and st[-1]=='(':
                    st.pop()
                else:
                    st.append(i)
        for i in st:
            if i=='(':
                a+=1
            else:
                b+=1
        def check_valid(arr):
            st=[]
            for i in arr:
                if i=='(':
                    st.append(i)
                elif i==')':
                    if st and st[-1]=='(':
                        st.pop()
                    else:
                        st.append(i)
            if st:
                return False
            else:
                return True
        
     
        def bt(i,sol,open_brace,closed_brace,open_,close_):
                    nonlocal ans
                    if i==len(s):
                        if check_valid(sol):
                            ans.add("".join(sol))
                        return 
                    if s[i]=='(' and open_brace < open_:
                        bt(i+1,sol,open_brace+1,closed_brace,open_,close_)
                    elif s[i]==')' and closed_brace < close_:
                        bt(i+1,sol,open_brace,closed_brace+1,open_,close_)
                    sol.append(s[i])
                    bt(i+1,sol,open_brace,closed_brace,open_,close_)
                    sol.pop()
        bt(0,[],0,0,a,b)
        return list(ans)
            