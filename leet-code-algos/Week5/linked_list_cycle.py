# linked list cycle
# https://leetcode.com/problems/linked-list-cycle/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        hash_map = {}
        while(head is not None):
            if head in hash_map:
                return True
            else:
                hash_map[head] = 1
                head = head.next
        return False