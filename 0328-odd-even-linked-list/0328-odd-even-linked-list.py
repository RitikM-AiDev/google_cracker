# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode | None) -> ListNode | None:
        if not head or not head.next:
            return head
        t1=head
        t2=head.next
        even = head.next
        while t1.next and t2.next:
            t1.next = t2.next
            t1 = t1.next
            t2.next = t1.next
            t2 = t2.next
        t1.next = even
        return head