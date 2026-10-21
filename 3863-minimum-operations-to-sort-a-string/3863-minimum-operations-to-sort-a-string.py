class Solution:
    def minOperations(self, s: str) -> int:
        min_=min(s)
        max_=max(s)
        if "".join(sorted(s))==s:
            return 0
        elif len(s)==2:
            return -1
        elif (s[0]==max_ and s[-1]==min_) and (s.count(max_) == 1 and s.count(min_) == 1):
            return 3
        elif s[0]==min_ or s[-1]==max_:
            return 1
        else:
            return 2