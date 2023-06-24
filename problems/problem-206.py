# Given the head of a singly linked list, reverse the list, and return the
# reversed list.

from typing import Optional

from core.list import ListNode
from helpers.list import ListHelper


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head

        previous = head
        current = head.next
        previous.next = None

        while current:
            next = current.next
            current.next = previous
            previous = current
            current = next

        return previous


helper = ListHelper()
list = helper.makeList([1, 2, 3, 4, 5])
helper.printList(list)

solution = Solution()
reservedList = solution.reverseList(list)
helper.printList(reservedList)
