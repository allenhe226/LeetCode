# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def reverse(head):
            prev, cur = None, head
            while cur:
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt
            return prev
        
        dummy = ListNode()
        tail = reverse(head)
        dummy.next = tail

        cur = dummy
        while n > 1:
            cur = cur.next
            n -= 1
        cur.next = cur.next.next
        return reverse(dummy.next)
        