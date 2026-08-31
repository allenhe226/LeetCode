# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        vals = []
        count = 0
        pre = None
        nxt = None
        
        cur = head
        while cur:
            nxt = cur.next if cur.next else None
            if pre and nxt and (cur.val > max(pre.val, nxt.val) or cur.val < min(pre.val, nxt.val)):
                vals.append(count)
            count += 1
            pre = cur
            cur = cur.next
        
        if len(vals) < 2:
            return [-1,-1]
        mn = float("inf")
        for i in range(len(vals)-1):
            mn = min(mn, vals[i+1]-vals[i])
        mx = vals[-1] - vals[0]
        return [mn, mx]


