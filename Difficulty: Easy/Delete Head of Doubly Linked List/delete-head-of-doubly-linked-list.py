''' Structure of doubly linked list Node
 class Node:
    def __init__(self, x):
        self.data = x
        self.next = None
        self.prev = None
'''
class Solution:
    def deleteHead(self, head):
        # code here
        if head is None:
            return None
        if head.next is None:
            return None
            
        head = head.next
        head.prev = None
        
        return head
        
            
        