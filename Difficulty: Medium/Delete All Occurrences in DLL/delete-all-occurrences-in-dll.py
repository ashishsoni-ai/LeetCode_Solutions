"""
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

"""
class Solution:
    def deleteAllOccurOfX(self, head, x):
        # code here
        temp = head
        new_head = head
        previous = None
        
        while temp is not None:
            if temp.data == x:
                if previous is not None:
                    previous.next = temp.next
                    
                    
                if temp.next is not None:
                    temp.next.prev = previous
                
                if temp == new_head:
                    new_head = new_head.next
                

            previous = temp
            temp = temp.next
            
        return new_head
        