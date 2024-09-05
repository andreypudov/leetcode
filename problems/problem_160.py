# 160. Intersection of Two Linked Lists
#
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
#
# Constraints:
#
# - The number of nodes of listA is in the m.
# -  The number of nodes of listB is in the n.
# - 1 <= m, n <= 3 * 10^4
# - 1 <= Node.val <= 10^5
# - 0 <= skipA < m
# - 0 <= skipB < n
# - intersectVal is 0 if listA and listB do not intersect.
# - intersectVal == listA[skipA] == listB[skipB] if listA and listB intersect.


from typing import Optional

from problems.core.list import ListNode


class Solution:
    def getIntersectionNode(
        self, headA: ListNode, headB: ListNode
    ) -> Optional[ListNode]:
        headA, headB = self.__truncate_same_length(headA, headB)

        while headA:
            if self.__is_intersected(headA, headB):
                return headA
            headA = headA.next
            headB = headB.next

    def __truncate_same_length(
        self, headA: ListNode, headB: ListNode
    ) -> tuple[ListNode, ListNode]:
        length_a = self.__get_list_length(headA)
        length_b = self.__get_list_length(headB)

        if length_a > length_b:
            headA = self.__truncate_to_length(headA, length_a - length_b)
        elif length_a < length_b:
            headB = self.__truncate_to_length(headB, length_b - length_a)

        return headA, headB

    def __truncate_to_length(self, head: ListNode, skip: int) -> ListNode:
        while skip:
            head = head.next
            skip -= 1

        return head

    def __is_intersected(self, head_a: ListNode, head_b: ListNode) -> bool:
        while head_a and head_b:
            if head_a.val == head_b.val:
                head_a = head_a.next
                head_b = head_b.next
            else:
                return False

        return head_a is None and head_b is None

    def __get_list_length(self, head: ListNode) -> int:
        length = 0

        while head:
            length += 1
            head = head.next

        return length
