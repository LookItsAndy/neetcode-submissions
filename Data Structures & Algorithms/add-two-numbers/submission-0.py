# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        carry = 0
        while l1 or l2 or carry:            # considering carry prevents edge cases (ex: 7+8)
            v1 = l1.val if l1 else 0        # set v1 to l1 if its not null else make 0  
            v2 = l2.val if l2 else 0


            # compute new digit
            val = v1 + v2 + carry

            carry = val // 10
            val = val % 10
            curr.next = ListNode(val)

            # update curr, l1, l2 pointers

            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None


        return dummy.next