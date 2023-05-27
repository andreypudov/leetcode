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
    # def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
    #     lenghtA = self.getListLenght(headA)
    #     lenghtB = self.getListLenght(headB)
    #     # return self.getIntersectionNodeWithLenghts(headA, headB, lenghtA, lenghtB)
    #     if lenghtA >= lenghtB:
    #         return self.getIntersectionNodeWithLenghts(headA, headB, lenghtA, lenghtB)
    #     else:
    #         return self.getIntersectionNodeWithLenghts(headB, headA, lenghtB, lenghtA)
    # def getIntersectionNodeWithLenghts(self, headLong:ListNode, headShort:ListNode, lenghtLong:int, lenghtSort:int):
    #     while headLong:
    #         # print(headLong.val, headShort.val)
    #         nodeWithSameValue = self.getNodeByValue(headLong.val, headShort)
    #         # print(nodeWithSameValue.val)
    #         if nodeWithSameValue:
    #             if self.isIntersected(headLong, nodeWithSameValue):
    #                 print(True)
    #                 return nodeWithSameValue
    #         headLong = headLong.next
    #         lenghtLong -= 1
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        headA, headB = self.truncateSameLenght(headA, headB)
        while headA:
            nodeWithSameValue = self.getNodeByValue(headA.val, headB)
            if nodeWithSameValue:
                if self.isIntersected(headA, nodeWithSameValue):
                    return nodeWithSameValue
            headA = headA.next


    def getNodeByValue(self, value: int, head: ListNode) -> Optional[ListNode]:
        while head:
            if head.val == value:
                return head
            head = head.next

    def truncateSameLenght(self, headA, headB):
        lenghtA = self.getListLenght(headA)
        lenghtB = self.getListLenght(headB)
        if lenghtA > lenghtB:
            headA = self.truncateToLenght(headA, lenghtA - lenghtB)
        elif lenghtA < lenghtB:
            headB = self.truncateToLenght(headB, lenghtB - lenghtA)
        return headA, headB

    def truncateToLenght(self, head, skip):
        while skip:
            head = head.next
            skip -= 1
        return head


    def isIntersected(self, headA: ListNode, headB: ListNode) -> bool:
        while headA and headB:
            print(headA.val, headB.val)
            if headA.val == headB.val:
                headA = headA.next
                headB = headB.next

            else:
                return False
        return headA == None and headB == None

    def getListLenght(self, head: ListNode) -> int:
        l = 0
        while head:
            l += 1
            head = head.next
        return l



helper = ListHelper()
head_a = helper.makeList([4,1,4,5])
head_b = helper.makeList([6,1,8,4,5])

helper.printList(head_a)
helper.printList(head_b)

solution = Solution()
intersectNode = solution.getIntersectionNode(head_a, head_b)
helper.printList(intersectNode)

