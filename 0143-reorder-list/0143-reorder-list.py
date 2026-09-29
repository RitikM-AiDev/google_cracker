# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode | None) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return
        i = head
        j = head
        while j.next and j.next.next:
            prev = i
            i = i.next
            j = j.next.next
        mid = i.next
        i.next=None
        prev=None
        i=mid
        while i:
            temp = i.next
            i.next = prev
            prev=i
            i = temp

        i = head
        j = prev
        while i and j:
            temp = i.next
            temp2 = j.next
            i.next = j
            j.next = temp
            i = temp
            j = temp2
    
        return head
        

            