from typing import List, Optional

from problems.core.list import ListNode


class ListHelper:
    def make_list(self, array: List[int]) -> Optional[ListNode]:
        if len(array) == 0:
            return None

        head: ListNode
        previous = None

        for index in range(len(array) - 1, -1, -1):
            element = array[index]
            current = ListNode(element, previous)

            previous = current

        head = previous
        return head

    def make_list_with_cycle(
        self, array: List[int], cycle_from_end_to: int
    ) -> Optional[ListNode]:
        head = self.make_list(array)
        if not head:
            return None

        tail = head
        length = 1
        while tail.next:
            tail = tail.next
            length += 1

        if 0 <= cycle_from_end_to <= length:
            steps = length - cycle_from_end_to
            cycle_start = head
            for _ in range(steps - 1):
                cycle_start = cycle_start.next
            tail.next = cycle_start

        return head

    def make_list2(self, array: List[List[int]]) -> List[Optional[ListNode]]:
        if len(array) == 0:
            return None

        result = []

        for element in array:
            result.append(self.make_list(element))

        return result

    def compare_lists(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> bool:
        while l1 and l2:
            if l1.val != l2.val:
                return False

            l1 = l1.next
            l2 = l2.next

        return l1 == l2

    def to_string(self, head: Optional[ListNode]) -> str:
        result = ""

        while head:
            result += str(head.val)
            head = head.next

        return result

    def print_list(self, head: Optional[ListNode], end: str = "\n"):
        print("[", end=" ")
        while head:
            print(head.val, end=" ")
            head = head.next
        print("]", end=end)

    def print_list2(self, lists: List[Optional[ListNode]]):
        if lists is None:
            print("[ ]")
            return

        print("[", end=" ")
        for node in lists:
            self.print_list(node, end=" ")
        print("]")
