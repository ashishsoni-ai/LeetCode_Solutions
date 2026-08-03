class Solution:
    def joinLists(self, head1, head2):
        
        # If first list is empty
        if head1 is None:
            return head2
        
        temp = head1
        
        # Go to the last node of first list
        while temp.next is not None:
            temp = temp.next
        
        # Join second list
        temp.next = head2
        
        return head1