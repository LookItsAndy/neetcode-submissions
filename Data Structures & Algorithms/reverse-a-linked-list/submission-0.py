# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def reverse(head):
            if head and head.next:
                prevHead = head.next
                tmp = reverse(head.next)
                head.next = None
                prevHead.next = head
                return tmp
                

            else: return head   # return head when it reaches end


        return reverse(head)