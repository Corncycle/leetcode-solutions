from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        count, curr = 1, head
        while curr.next:
            count += 1
            curr = curr.next
        mid, curr = count // 2, head
        for i in range(mid):
            curr = curr.next
        return curr