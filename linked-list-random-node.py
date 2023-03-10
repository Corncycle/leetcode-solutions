from typing import Optional
from random import randrange

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def __init__(self, head: Optional[ListNode]):
        curr = head
        self.head = head
        self.length = 0
        while curr:
            self.length += 1
            curr = curr.next

    def getRandom(self) -> int:
        i = randrange(self.length)
        curr = self.head
        for _ in range(i):
            curr = curr.next
        return curr.val
