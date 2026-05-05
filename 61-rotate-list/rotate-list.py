# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        x = head
        n = 0
        while x:
            n += 1
            if not x.next:
                x.next = head
                break
            x = x.next
        
        if n == 0:
            return head
        
        for i in range(n-k%n-1):
            head = head.next
        root = head.next;
        head.next = None
        return root

        