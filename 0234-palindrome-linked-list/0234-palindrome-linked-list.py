# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        st=[]
        t1 = head
        t2 = head
        l = 0
        if head==None or head.next==None:
            return True
        while t2 and t2.next:
                st.append(t1.val)
                t1 = t1.next
                t2 = t2.next.next
                l+=2
        while t1:
            if st and t1.val == st[-1]:
                st.pop()
            t1 = t1.next
        print(st)
        if st:
            return False
        return True
        
        
        
        