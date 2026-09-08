''' Structure of linked list Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''
class Solution:
    def getCount(self, head):
        # code here
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
        return length
        