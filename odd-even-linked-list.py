from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __repr__(self) -> str:
        return f"(val: {self.val}, next: {self.next})"

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        curr = head.next.next
        tailOdd = head
        headEven = head.next
        tailEven = head.next
        oddStep = True
        while curr:
            if oddStep:
                tailOdd.next = curr
                tailOdd = tailOdd.next
            else:
                tailEven.next = curr
                tailEven = tailEven.next
            oddStep = not oddStep
            curr = curr.next
        tailOdd.next = headEven
        tailEven.next = None
        return head