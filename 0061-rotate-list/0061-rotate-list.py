# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode | None, k: int) -> ListNode | None:
            if not head or not head.next:
                return head
            l=0
            temp=head
            while temp:
                prev = temp
                l+=1
                temp = temp.next
            prev.next = head
            k =k%l
            finish = l - k
            curr=0
            temp = prev
            while finish!=curr:
                temp = temp.next
                curr+=1
            target = temp.next
            temp.next= None
            return target

