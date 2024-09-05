from typing import Optional, overload

from problems.core.list import ListNode


class ListHelper:
    def make_list(self, array: list[int]) -> Optional[ListNode]:
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

    def make_list2(self, array: list[list[int]]) -> list[Optional[ListNode]]:
        if len(array) == 0:
            return None

        result = []

        for element in array:
            result.append(self.make_list(element))

        return result

    def compare_lists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> bool:
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

    def print_list2(self, lists: list[Optional[ListNode]]):
        if lists is None:
            print("[ ]")
            return

        print("[", end=" ")
        for node in lists:
            self.print_list(node, end=" ")
        print("]")
