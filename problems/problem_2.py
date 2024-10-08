# 2. Add Two Numbers
#
# You are given two non-empty linked lists representing two non-negative
# integers. The digits are stored in reverse order, and each of their nodes
# contains a single digit. Add the two numbers and return the sum as a linked
# list. You may assume the two numbers do not contain any leading zero, except
# the number 0 itself.
#
# Constraints:
#
# - The number of nodes in each linked list is in the range [1, 100].
# - 0 <= Node.val <= 9
# - It is guaranteed that the list represents a number that does not have
#   leading zeros.


from typing import Optional

from problems.core.list import ListNode


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        result = ListNode(0)
        result_tail = result
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            carry, out = divmod(val1 + val2 + carry, 10)

            result_tail.next = ListNode(out)
            result_tail = result_tail.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return result.next
