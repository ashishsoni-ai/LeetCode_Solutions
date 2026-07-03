''' Structure of linked list Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''
class Solution:
    def getCount(self, head):
        # code here
        count =  head
        l = 0
        while count != None:
            count = count.next
            l +=1
        return l