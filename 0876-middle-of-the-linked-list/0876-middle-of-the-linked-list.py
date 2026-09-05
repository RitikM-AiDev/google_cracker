# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, root: Optional[ListNode]) -> Optional[ListNode]:
            head = root
            i = root
            j = root
            k=0
            d=0
            while j and j.next:
                print(k,d)
                k+=1
                d+=2
                i = i.next
                j = j.next.next
            return i
                

