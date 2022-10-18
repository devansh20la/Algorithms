# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        i = j = head
        gap = 0
        
        while(i.next is not None):
            i = i.next
            gap +=1
            
            if gap > n:
                j = j.next
        
        if gap < n:
            return head.next
        
        t = j.next.next if j.next.next else None
        j.next = t

        return head
            
        