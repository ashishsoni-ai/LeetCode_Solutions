'''
# Node Class    
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
'''
class Solution:
    def areIdentical(self, head1, head2):
        # Code here
        curr1 = head1
        curr2 = head2
        res1 = []
        res2 = []
        
        while curr1 is not None:
            res1.append(curr1.data)
            curr1 = curr1.next
        while curr2 is not None :
            res2.append(curr2.data)
            curr2 = curr2.next
            
        if res1 == res2:
            return True
        else:
            return False
        
        
        