# reverse linked list
# https://leetcode.com/problems/reverse-linked-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        i = None
        j = head
        if j is None or j.next is None:
            return j
        else:
            while(j is not None):
                k = j.next
                j.next = i
                i = j
                j = k
        return i