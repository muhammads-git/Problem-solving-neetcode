# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# class Solution:
#     def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

#         dummy = ListNode()
#         dummy.next = head
#         prev = dummy

#         while True:
#             curr = head

#             for i in range(k):
#                 if curr is None:
#                     return dummy.next
#                 curr = curr.next

#             #
#             group_head = head
#             prev_node = None
#             tail=head

#             for i in range(k):
#                 nxt = group_head.next
#                 group_head.next = prev_node
#                 prev_node = group_head
#                 group_head = nxt
                
          
#             #
#             prev.next = prev_node
#             tail.next = curr
#             prev = tail
#             head = curr

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        cur = head
        for _ in range(k):
            if not cur:
                return head
            cur = cur.next

        prev = self.reverseKGroup(cur, k)
        cur = head
        for _ in range(k):
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        return prev
