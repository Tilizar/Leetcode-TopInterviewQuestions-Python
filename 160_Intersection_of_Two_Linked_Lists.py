from typing import Optional

from utils.ListNode import ListNode


def getIntersectionNode(headA: ListNode, headB: ListNode) -> Optional[ListNode]:
    left, right = headA, headB

    while left is not right:
        left = left.next if left else headB
        right = right.next if right else headA

    return left


def case_1():
    common = ListNode(8, next=ListNode(4, next=ListNode(5)))
    first = ListNode(4, next=ListNode(1, next=common))
    second = ListNode(5, next=ListNode(6, next=ListNode(1, next=common)))

    assert common == getIntersectionNode(first, second)


def case_2():
    common = ListNode(2, next=ListNode(4))
    first = ListNode(1, next=ListNode(9, next=ListNode(1, next=common)))
    second = ListNode(3, next=common)

    assert common == getIntersectionNode(first, second)


def case_3():
    first = ListNode(2, next=ListNode(6, next=ListNode(4)))
    second = ListNode(3, next=ListNode(5))

    assert None == getIntersectionNode(first, second)


if __name__ == '__main__':
    case_1()
    case_2()
    case_3()
