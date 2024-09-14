# 23. Merge k Sorted Lists
#
# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
#
# Merge all the linked-lists into one sorted linked-list and return it.

from typing import Optional

from problems.core.list import ListNode


class Solution:
    def mergeKLists(
        self, lists: list[Optional[ListNode]]
    ) -> Optional[ListNode]:
        head = None
        current = None

        while lists:
            min_value = float("inf")
            min_index = -1

            for index, node in enumerate(lists):
                if node is None:
                    continue
                if node.val < min_value:
                    min_value = node.val
                    min_index = index

            if min_index == -1:
                break

            min_node = ListNode(min_value)
            if head is None:
                head = min_node
                current = head
            else:
                current.next = min_node
                current = min_node

            lists[min_index] = lists[min_index].next
            if lists[min_index] is None:
                lists.pop(min_index)

        return head
