from typing import Optional

from utils.ListNode import ListNode


def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode()
    pointer = dummy

    has_carry = False
    while l1 or l2 or has_carry:
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0

        sum = val1 + val2 + (1 if has_carry else 0)
        has_carry = sum >= 10

        pointer.next = ListNode(sum % 10)
        pointer = pointer.next

        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None

    return dummy.next


def case_1():
    first = ListNode(2, next=ListNode(4, next=ListNode(3)))
    second = ListNode(5, next=ListNode(6, next=ListNode(4)))

    expected = ListNode(7, next=ListNode(0, next=ListNode(8)))

    assert expected == addTwoNumbers(first, second)


def case_2():
    assert ListNode(0) == addTwoNumbers(ListNode(0), ListNode(0))


def case_3():
    first = ListNode(9, next=ListNode(9, next=ListNode(9, next=ListNode(9, next=ListNode(9, next=ListNode(9, next=ListNode(9)))))))
    second = ListNode(9, next=ListNode(9, next=ListNode(9, next=ListNode(9))))

    expected = ListNode(8, next=ListNode(9, next=ListNode(9, next=ListNode(9, next=ListNode(0, next=ListNode(0, next=ListNode(0, next=ListNode(1))))))))

    assert expected == addTwoNumbers(first, second)


if __name__ == '__main__':
    case_1()
    case_2()
    case_3()
