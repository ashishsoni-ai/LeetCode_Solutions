"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        if head == None:
            return head
        p = head

        while p != None:
            if p.child == None:
                p = p.next
            else:
                #ab link ko change karna hain
                temp = p.child
                while temp.next != None:
                    temp = temp.next
                if p.next != None:
                    temp.next = p.next
                    p.next.prev = temp

                p.next = p.child
                p.child.prev = p
                p.child = None
                

        return head

        