# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        dummy = ListNode()
        dummy.next = head
        prev = dummy
        curr = head
        L = 0
        
        # good
        steps = 0
        while curr != None:
            curr = curr.next
            L = L + 1

        steps = L - n
        for i in range(steps):
            prev = prev.next

        prev.next = prev.next.next
        prev=prev.next

        return dummy.next
