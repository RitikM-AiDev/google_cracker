class Solution:
    def removeDuplicates(self, l: List[int]) -> int:
        i = 0
        j = 1
        while j < len(l):
            print(i, j)

            if l[i] == l[j]:
                j += 1
            else:
                i += 1
                l[i]=l[j]
                j += 1

        return i+1