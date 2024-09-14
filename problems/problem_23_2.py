# 23. Merge k Sorted Lists
#
# You are given an array of k linked-lists lists, each linked-list is sorted in
# ascending order.
#
# Merge all the linked-lists into one sorted linked-list and return it.

from typing import Optional

from problems.core.list import ListNode


class Solution:
    def mergeKLists(
        self, lists: list[Optional[ListNode]]
    ) -> Optional[ListNode]:
        elements = self.__make_sorted_list(lists)

        return self.__make_linked_list(elements)

    def __make_sorted_list(self, lists: list[Optional[ListNode]]) -> list[int]:
        unsorted_list = []

        if not lists:
            return unsorted_list

        for node in lists:
            head = node

            while head is not None:
                unsorted_list.append(head.val)
                head = head.next

        return sorted(unsorted_list)

    def __make_linked_list(self, elements: list[int]) -> Optional[ListNode]:
        head = None
        current = None

        for element in elements:
            if head is None:
                head = ListNode(element)
                current = head
            else:
                current.next = ListNode(element)
                current = current.next

        return head
