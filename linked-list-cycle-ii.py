from util import ListNode
from typing import Optional

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        visited = {id(head)}
        curr = head
        while curr.next:
            if id(curr.next) in visited:
                return curr.next
            visited.add(id(curr.next))
            curr = curr.next
        return None