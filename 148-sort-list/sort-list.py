# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def mergeTwoSortedLinkedLists(self, list1, list2):
        dummy = ListNode(-1)
        temp = dummy

        while list1 and list2:

            if list1.val <= list2.val:
                temp.next = list1
                list1 = list1.next
            else:
                temp.next = list2
                list2 = list2.next

            temp = temp.next

        if list1:
            temp.next = list1
        else:
            temp.next = list2

        return dummy.next


    def sortlist(self, head):

        # Empty list or one node
        if head is None or head.next is None:
            return head

        slow = head
        fast = head.next

        # Find middle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Split list
        right = slow.next
        slow.next = None

        # Sort both halves
        left = self.sortlist(head)
        right = self.sortlist(right)

        # Merge
        return self.mergeTwoSortedLinkedLists(left, right)


    def sortList(self, head):
        return self.sortlist(head)



        # temp = head
        # ans = []
        # while temp is not None:
        #     ans.append(temp.val)
        #     temp = temp.next
        # ans.sort()
        # temp = head
        # for value in ans:
        #     temp.val = value
        #     temp = temp.next

        # return head



        