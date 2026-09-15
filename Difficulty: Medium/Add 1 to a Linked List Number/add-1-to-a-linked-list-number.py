''' structure of linked list Node
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
'''
class Solution:
    def reverse(self,head):
        prev = None
        curr = head
        while curr != None:
            forward = curr.next
            curr.next = prev
            prev = curr
            curr = forward
        return prev
        
    def addOne(self,head):
        #reverse the node
        head = self.reverse(head)
        curr = head
        carry = 1
        while curr != None:
            nodevalue = curr.data
            sum = carry + nodevalue
            
            digit = sum%10
            curr.data = digit
            #carry kitna bacha 
            carry = sum//10
           
           
            # solving case jaha sari node 999 ho or +1 kare tho 1000 ho jaye or new node add karni pade last mai
            if curr.next == None and carry > 0:
                curr.next = Node(carry)
                carry = 0
                break
            #curr ko aga badhana hain
            curr = curr.next
        head = self.reverse(head)
        
        return head
            
            
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        