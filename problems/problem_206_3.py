# 206. Reverse Linked List
#
# Given the head of a singly linked list, reverse the list, and return the
# reversed list.
#
# Constraints:
#
# - The number of nodes in the list is the range [0, 5000].
# - -5000 <= Node.val <= 5000

from typing import Optional

from problems.core.list import ListNode


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        stack = []

        while head:
            stack.append(head)
            head = head.next

        newHead = stack.pop()
        current = newHead

        while stack:
            node = stack.pop()
            current.next = node
            current = node

        current.next = None
        return newHead
