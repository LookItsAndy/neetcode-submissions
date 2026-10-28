# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        

        # use recursion: helps get to the end before actually reversing the linked list


        def reverse(head):

            if head and head.next:
                next_head = head.next
                tmp = reverse(head.next)
                head.next = None
                next_head.next = head
                return tmp
            return head

        return reverse(head)