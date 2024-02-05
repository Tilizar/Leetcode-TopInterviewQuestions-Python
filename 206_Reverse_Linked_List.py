from typing import Optional

from utils.ListNode import ListNode


def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head:
        return None

    new_head = head
    if head.next:
        new_head = reverseList(head.next)
        head.next.next = head
    head.next = None

    return new_head


def case_1():
    list_node = ListNode(1, next=ListNode(2, next=ListNode(3, next=ListNode(4, next=ListNode(5)))))
    output = reverseList(list_node)
    expected = ListNode(5, next=ListNode(4, next=ListNode(3, next=ListNode(2, next=ListNode(1)))))
    assert expected == output


def case_2():
    list_node = ListNode(1, next=ListNode(2))
    output = reverseList(list_node)
    expected = ListNode(2, next=ListNode(1))
    assert expected == output


def case_3():
    output = reverseList(None)
    assert output is None


if __name__ == '__main__':
    case_1()
    case_2()
    case_3()
