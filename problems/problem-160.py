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
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        headA, headB = self.truncateSameLength(headA, headB)

        while headA:
            if self.isIntersected(headA, headB):
                return headA
            headA = headA.next
            headB = headB.next

    def truncateSameLength(self, headA: ListNode, headB: ListNode) -> tuple[ListNode, ListNode]:
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

        return headA == None and headB == None

    def getListLength(self, head: ListNode) -> int:
        length = 0

        while head:
            length += 1
            head = head.next

        return length

helper = ListHelper()
headA = helper.makeList([4,1,8,4,5])
headB = helper.makeList([5,6,1,8,4,5])

helper.printList(headA)
helper.printList(headB)

solution = Solution()
intersectNode = solution.getIntersectionNode(headA, headB)
helper.printList(intersectNode)

