"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        
        ptr = head;
        
        # put cloned nodes next to old nodes
        while ptr:
            new_node = Node(ptr.val, None, None)
            
            new_node.next = ptr.next
            ptr.next = new_node
            ptr = new_node.next
        
        ptr = head
        
        # now link random pointers
        while ptr:
            ptr.next.random = ptr.random.next if ptr.random else None
            ptr = ptr.next.next
        
        #unweave the linked list
        ptr_old_list = head
        ptr_new_list = head.next
        head_new = head.next
        while ptr_old_list:
            ptr_old_list.next = ptr_old_list.next.next
            ptr_new_list.next = ptr_new_list.next.next if ptr_new_list.next else None
            
            ptr_old_list = ptr_old_list.next
            ptr_new_list = ptr_new_list.next
        
        return head_new

# class Solution:
#     def __init__(self):
#         self.hashmap = {}
    
#     def getclonednode(self, p):
#         if p:
#             if p in self.hashmap:
#                 return self.hashmap[p]
#             else:
#                 t = Node(p.val, None, None)
#                 self.hashmap[p] = t
#                 return self.hashmap[p]
#         else:
#             return None
    
    
#     def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
#         if head is None:
#             return None
        
#         p = head
#         dummy = dummy_head = Node(p.val, None, None)
#         self.hashmap[p] = dummy
#         while (p is not None):
            
#             dummy.random = self.getclonednode(p.random)
#             dummy.next = self.getclonednode(p.next)
            
#             dummy = dummy.next
#             p = p.next

#         return dummy_head
        