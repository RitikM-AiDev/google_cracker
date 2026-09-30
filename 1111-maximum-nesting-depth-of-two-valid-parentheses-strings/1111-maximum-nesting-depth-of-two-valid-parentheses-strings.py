class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        depth=0
        dep = []
        for i in seq:
            if i=='(':
                depth = 1 - depth
                dep.append(depth)   
            else:
                dep.append(depth)
                depth = 1 - depth
        return dep