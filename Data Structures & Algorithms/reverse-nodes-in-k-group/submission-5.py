# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # reverse in chunks
        # need to have k left to reverse
        # find lenght

        dummy = ListNode()
        dummy.next = head
        prev = dummy 

        while True:

            curr = head
            group_head = curr

            for i in range(k):
                if curr is None:
                    return dummy.next

                curr = curr.next
            # now curr is on next groups head
            # revers from group head
            prev_node = None
            curr_node = group_head

            for i in range(k):
                nxt = curr_node.next
                curr_node.next = prev_node
                prev_node = curr_node
                curr_node = nxt
            # 
            prev.next = prev_node
            group_head.next = curr
            prev=group_head
            head = curr

        



