# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #  two pointers cold solving is pending....

        dummy = ListNode()
        dummy.next = head
        curr = head
        right=curr
        left=dummy

        for i in range(n):
            right = right.next
        
        while right is not None:
            right = right.next
            left = left.next
        
        left.next = left.next.next

        return dummy.next