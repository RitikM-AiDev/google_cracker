# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode | None, x: int) -> ListNode | None:
            a = None
            b= None
            at = None
            bt = None
            i = head
            while i:
                if i.val <x:
                    if a is None:
                        a = i
                        at=i
                    else:
                        at.next = i
                        at=at.next
                else:
                    if b is None:
                        b =i
                        bt=i
                    else:
                        bt.next = i
                        bt = bt.next
                i= i.next
            if bt:
                bt.next = None
            if a is None:
                return b
            elif b is None:
                return a
            else:
                at.next = b
                return a
