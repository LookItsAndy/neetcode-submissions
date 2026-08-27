# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        # neetcode follow along solution

        # base case if list is 0 or 1 nodes
        if not head or not head.next:
            return head

        
        left = head
        right = self.findMid(head)
        tmp = right.next
        right.next = None
        right = tmp

        # sort smaller lists (splits and merges)

        left = self.sortList(left)      # run until base case met. only one element in list then merge
        right = self.sortList(right)
        return self.merge(left, right)


    def findMid(self, head):
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next            # slow goes up one node at a time
            fast = fast.next.next       # fast goes up two nodes at a time
            # slow will stop at mid point because fast reaches end first
        return slow


    def merge(self, left, right):
        tail = headPtr = ListNode()

        while left and right:
            if left.val < right.val:
                tail.next = left
                left = left.next        # shift to next nodes
                
            else:
                tail.next = right
                right = right.next

            tail = tail.next


            # handle if uneven amounts of elements between two lists. last value automatically added to the end
        if left:
            tail.next = left
        if right:
            tail.next = right

        return headPtr.next