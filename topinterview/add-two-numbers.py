# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        out = None
        
        while l1 != None or l2 != None or carry != 0:
            s = 0
            if l1 is not None:
                s += l1.val
            if l2 is not None:
                s += l2.val
            
            s += carry
            carry = s // 10
            if out is None:
                out = ListNode(s % 10)
                origin = out
            else:
                out.next = ListNode(s % 10)
                out = out.next
            
            if l1 is not None:
                l1 = l1.next
            else:
                l1 = None
            if l2 is not None:
                l2 = l2.next
            else:
                l2 = None
        return origin
            
        