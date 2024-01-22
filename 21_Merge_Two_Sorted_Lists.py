from typing import Optional

from utils.ListNode import ListNode


def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode(0)
    pointer = dummy

    while list1 and list2:
        if list1.val < list2.val:
            pointer.next = list1
            list1 = list1.next
        else:
            pointer.next = list2
            list2 = list2.next

        pointer = pointer.next

    pointer.next = list1 or list2

    return dummy.next


if __name__ == '__main__':
    first2 = ListNode.from_list([1, 2, 4])
    second2 = ListNode.from_list([1, 3, 4])
    expected2 = ListNode.from_list([1, 1, 2, 3, 4, 4])
    assert  expected2 == mergeTwoLists(first2, second2)
