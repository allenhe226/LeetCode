# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(head):
            prev, cur = None, head
            while cur:
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt
            return prev
        
        def add(l1, l2):
            dummy = ListNode()
            cur = dummy
            carry = False
            while l1 or l2 or carry:
                v1 = l1.val if l1 else 0
                v2 = l2.val if l2 else 0

                val = v1 + v2 + 1 * carry
                cur.next = ListNode(val % 10)
                carry = True if val > 9 else False
                
                l1 = l1.next if l1 else None
                l2 = l2.next if l2 else None
                cur = cur.next
            return dummy.next
        return reverse(add(reverse(l1), reverse(l2)))