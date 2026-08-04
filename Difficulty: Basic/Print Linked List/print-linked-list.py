'''
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None
'''

class Solution:
    def printList(self, head):
        # code here
        temp = head
        ans = []
        while temp != None:
            ans.append(temp.data)
            temp = temp.next
        return ans
            