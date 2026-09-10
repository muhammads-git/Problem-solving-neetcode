# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()

        # rewise and goo next..
        def merge_two(l1:ListNode,l2:ListNode):
            curr = dummy
    
            while l1 and l2:
                if not l1 is None and not l2 is None: # unnecassary check?
                    if l1.val < l2.val:
                        curr.next = l1
                        curr = curr.next
                        l1 = l1.next
                    elif l1.val > l2.val:
                        curr.next = l2
                        curr = curr.next
                        l2 = l2.next
                    else:
                        curr.next = l1 
                        curr = curr.next
                        l1 = l1.next

            curr.next = l1 or l2
            curr = curr.next

            return dummy.next

        # base case
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]
        #
        mid = len(lists) // 2 
        left = lists[:mid]
        right = lists[mid:]

        # recursive case
        merged_left = self.mergeKLists(left)
        merged_right = self.mergeKLists(right)

        # left [], right []
        return merge_two(merged_left,merged_right)



