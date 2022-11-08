''' The commented approach below was somewhat slow. I assumed it was because of
    the slices and concatenation, so I tried adapting the approach to a
    linked list so that removal of a character would amount to moving pointers,
    rather than concatenating sliced strings. It does not seem conclusively
    faster.
'''

'''def makeGood(self, s: str) -> str:
        i = 0
        while i < len(s) - 1:
            print(s)
            if s[i].upper() == s[i+1].upper() and s[i] != s[i+1]:
                s = s[:i] + s[i+2:]
                i = max(0, i - 1)
            else:
                i += 1
        return s'''

class Node:
    def __init__(self, value: str):
        self.value = value
        self.next = None
        self.prev = None

    def __str__(self) -> str:
        return self.value    

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value: str):
        if self.head is None:
            self.head = Node(value)
            self.tail = self.head
        else:
            self.tail.next = Node(value)
            self.tail.next.prev = self.tail
            self.tail = self.tail.next
        return self.tail

    def remove(self, node: Node):
        if self.head == self.tail:
            self.head = None
            self.tail = None
        elif node == self.head:
            self.head = self.head.next
            self.head.prev = None
        elif node == self.tail:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            node.prev.next = node.next
            node.next.prev = node.prev

    def __str__(self) -> str:
        curr = self.head
        outStr = ""
        while curr is not None:
            outStr += curr.value
            curr = curr.next
        return outStr

class Solution:
    def makeGood(self, s: str) -> str:
        if len(s) <= 1:
            return s
        strList = LinkedList()
        for char in s:
            strList.append(char)
        curr = strList.head
        while curr is not None and curr.next is not None:
            if curr.value.upper() == curr.next.value.upper() and curr.value != curr.next.value:
                wasHead = curr == strList.head
                strList.remove(curr.next)
                strList.remove(curr)
                if wasHead:
                    curr = strList.head
                else:
                    curr = curr.prev
            else:
                curr = curr.next
        return str(strList)