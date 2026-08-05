# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        if not head :
            return []

        curr=head
        nodes = []
        while curr is not None:
            nodes.append(curr)
            curr = curr.next
        
        i = 0
        j = len(nodes) - 1

        while i < j:
            nodes[i].next = nodes[j]
            i += 1
            if i >= j:
                break
            nodes[j].next = nodes[i]
            j -= 1
            nodes[j].next = None
