from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class ListHelper:
    def makeList(self, array) -> ListNode:
        head: ListNode
        previous = None

        for index in range(len(array) - 1, -1, -1):
            element = array[index]
            current = ListNode(element, previous)

            previous = current

        head = previous
        return head

    def printList(self, head: Optional[ListNode]):
        print("[", end = " ")
        while head:
            print(head.val, end = " ")
            head = head.next
        print("]")

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

helper.printList(helper.makeList([1]))
helper.printList(helper.makeList([]))