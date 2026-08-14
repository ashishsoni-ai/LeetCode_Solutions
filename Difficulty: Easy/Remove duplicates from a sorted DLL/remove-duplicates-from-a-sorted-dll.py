class Solution:
    def removeDuplicates(self, head):
        temp = head

        while temp and temp.next:
            nextNode = temp.next

            # Find the next different node
            while nextNode and nextNode.data == temp.data:
                nextNode = nextNode.next

            # Remove duplicates
            temp.next = nextNode

            if nextNode:
                nextNode.prev = temp

            # Move to next distinct node
            temp = temp.next

        return head