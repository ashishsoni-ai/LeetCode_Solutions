'''    
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

class Solution:
    def insertAtEnd(self, head, x):
        #code here
        newNode = Node(x)
        if head is None:
            return newNode
        
        curr = head
        while curr.next:
            curr = curr.next
        curr.next = newNode
        newNode.next = None
        return head