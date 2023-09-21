from typing import Optional

from core.list import ListNode


class ListHelper:
    def makeList(self, array: [int]) -> ListNode:
        head: ListNode
        previous = None

        for index in range(len(array) - 1, -1, -1):
            element = array[index]
            current = ListNode(element, previous)

            previous = current

        head = previous
        return head

    def compareList(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> bool:
        while l1 and l2:
            if l1.val != l2.val:
                return False

            l1 = l1.next
            l2 = l2.next

        return l1 == l2

    def printList(self, head: Optional[ListNode]):
        print("[", end=" ")
        while head:
            print(head.val, end=" ")
            head = head.next
        print("]")
