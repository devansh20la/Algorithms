# Copy linked list
# https://leetcode.com/problems/copy-list-with-random-pointer

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution:
    def __init__(self):
        # old_node : new_node
        self.hash_map = {}
        
    def copyRandomList(self, head: 'Node') -> 'Node':

        if head is None:
            return None
        
        if head in self.hash_map:
            return self.hash_map[head]
        
        h = Node(head.val, None, None)
        self.hash_map[head] = h
            
        h.next = self.copyRandomList(head.next)
        h.random = self.copyRandomList(head.random)
        
        return h
        