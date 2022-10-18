# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = dummy_head = ListNode(0)
        p = list1
        q = list2
        
        while(p is not None and q is not None):
            if p.val < q.val:
                dummy.next = p
                p = p.next
            else:
                dummy.next = q
                q = q.next
            
            dummy = dummy.next
        
        if p is None:
            dummy.next = q
        else:
            dummy.next = p

        return dummy_head.next
            
        