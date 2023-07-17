from typing import Optional
from util import ListNode
from collections import deque

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def getNumFromLL(ll):
            num = 0
            curr = ll
            while curr:
                num += curr.val
                curr = curr.next
                if curr:
                    num *= 10
            return num
        
        n1 = getNumFromLL(l1)
        n2 = getNumFromLL(l2)

        total = n1 + n2
        totalDeque = deque()

        while total:
            totalDeque.appendleft(total % 10)
            total = total // 10

        if not totalDeque:
            return ListNode(0)

        curr = ListNode(totalDeque[0])
        head = curr

        for i in range(1, len(totalDeque)):
            curr.next = ListNode(totalDeque[i])
            curr = curr.next

        return head