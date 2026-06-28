# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        cur = head
        for i in range(k):
            if not cur:
                return head
            if i != k-1:
                cur = cur.next
            else:
                nxt = cur.next
                cur.next = None
                cur = nxt
        
        prev, cur = self.reverseKGroup(cur, k), head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        return prev