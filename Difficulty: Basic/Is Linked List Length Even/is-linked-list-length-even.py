"""
structure of link list node
class Node:
    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None
        
"""    
class Solution:
    
    def isEven(self, head):
        # Code here
        curr = head
        count = 0
        while curr is not None:
            count += 1
            curr = curr.next
        if count%2 == 0:
            return True
        else:
            return False
        