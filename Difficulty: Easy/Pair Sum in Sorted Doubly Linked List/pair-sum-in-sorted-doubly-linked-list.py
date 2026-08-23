# Structure of Doubly Linked List Node
'''
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None
'''

class Solution:
    def givenSumPairs(self, head, target):
        # code here
        # temp1 = head
        # ans = []
        
        # while temp1 and temp1.next:
        #     temp2 = temp1.next
            
        #     while temp2 is not None and temp1.data + temp2.data<=target:
        #         if temp1.data + temp2.data == target:
        #             ans.append([temp1.data,temp2.data])
        #         temp2 = temp2.next
        #     temp1 = temp1.next
            
        # return ans
        
        left = head
        right = head
        ans = []
        while right.next is not None:
            right = right.next

        while left.data<right.data:
            if left.data+right.data==target:
                ans.append([left.data,right.data])
                left = left.next
                right = right.prev
            elif left.data+right.data < target:
                left = left.next
            else:
                right = right.prev
        return ans
                
                    
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        