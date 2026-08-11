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
        current = head
        
        while current.next != None:
            current = current.next
        current.next = newNode

        return head
            