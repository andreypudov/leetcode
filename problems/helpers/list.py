from core.list import ListNode
from typing import Optional

class ListHelper:
    def makeList(self, array) -> ListNode:
        head: ListNode
        previous = None

        for index in range(len(array) - 1, -1, -1):
            element = array[index]
            current = ListNode(element, previous)

            previous = current

        head = previous
        return head

    def printList(self, head: Optional[ListNode]):
        print("[", end = " ")
        while head:
            print(head.val, end = " ")
            head = head.next
        print("]")
