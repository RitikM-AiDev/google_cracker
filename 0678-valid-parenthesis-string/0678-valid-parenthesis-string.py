class Solution:
    def checkValidString(self, s: str) -> bool:
        st=[]
        op=[]
        f= {")" : "("}
        opf = {}
        c=0
        for i in range(len(s)):
            if s[i] in "(":
                st.append(s[i])
                if s[i] not in opf:
                    opf[s[i]] = [i]
                else:
                    opf[s[i]].append(i)
            elif s[i]=="*":
                op.append(i)
            else:
                if st and st[-1] == f[s[i]]:
                    if st[-1] in opf and opf[st[-1]]:
                        opf[st[-1]].pop()
                        if not opf[st[-1]]:
                            del opf[st[-1]]
                    st.pop()
                else:
                    if op:
                        op.pop()
                    else:
                        st.append(s[i])
                        if s[i] not in opf:
                            opf[s[i]] = [i]
                        else:
                            opf[s[i]].append(i)
        fl=0
        if ")" in opf:
            return False
        if "(" in opf:
            v = opf["("]
            while v:
                if not op:
                    return False
                n1 = op.pop()
                n2 = v.pop()
                if n1 < n2:
                    fl=1
        if fl:
            return False
        return True
