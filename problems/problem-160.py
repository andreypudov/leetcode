# Given the heads of two singly linked-lists headA and headB, return the node at
# which the two lists intersect. If the two linked lists have no intersection at
# all, return null.
#
# For example, the following two linked lists begin to intersect at node c1:
#
# The test cases are generated such that there are no cycles anywhere in the
# entire linked structure.
#
# Note that the linked lists must retain their original structure after the
# function returns.
#
# Custom Judge:
#
# The inputs to the judge are given as follows (your program is not given these
# inputs):
#
#    intersectVal - The value of the node where the intersection occurs. This is
#                   0 if there is no intersected node.
#    listA - The first linked list.
#    listB - The second linked list.
#    skipA - The number of nodes to skip ahead in listA (starting from the head)
#            to get to the intersected node.
#    skipB - The number of nodes to skip ahead in listB (starting from the head)
#            to get to the intersected node.
#
# The judge will then create the linked structure based on these inputs and pass
# the two heads, headA and headB to your program. If you correctly return the
# intersected node, then your solution will be accepted.

from typing import Optional

from core.list import ListNode
from helpers.list import ListHelper


class Solution:
    def getIntersectionNode(
        self, headA: ListNode, headB: ListNode
    ) -> Optional[ListNode]:
        headA, headB = self.truncateSameLength(headA, headB)

        while headA:
            if self.isIntersected(headA, headB):
                return headA
            headA = headA.next
            headB = headB.next

    def truncateSameLength(
        self, headA: ListNode, headB: ListNode
    ) -> tuple[ListNode, ListNode]:
        lengthA = self.getListLength(headA)
        lengthB = self.getListLength(headB)

        if lengthA > lengthB:
            headA = self.truncateToLength(headA, lengthA - lengthB)
        elif lengthA < lengthB:
            headB = self.truncateToLength(headB, lengthB - lengthA)

        return headA, headB

    def truncateToLength(self, head: ListNode, skip: int) -> ListNode:
        while skip:
            head = head.next
            skip -= 1

        return head

    def isIntersected(self, headA: ListNode, headB: ListNode) -> bool:
        while headA and headB:
            if headA.val == headB.val:
                headA = headA.next
                headB = headB.next
            else:
                return False

        return headA is None and headB is None

    def getListLength(self, head: ListNode) -> int:
        length = 0

        while head:
            length += 1
            head = head.next

        return length


helper = ListHelper()
headA = helper.makeList([4, 1, 8, 4, 5])
headB = helper.makeList([5, 6, 1, 8, 4, 5])

helper.printList(headA)
helper.printList(headB)

solution = Solution()
intersectNode = solution.getIntersectionNode(headA, headB)
helper.printList(intersectNode)
