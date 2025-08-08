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
        if head is None or head.next is None:
            return head

        newHead = self.reverseList(head.next)
        head.next.next = head
        head.next = None

        return newHead
