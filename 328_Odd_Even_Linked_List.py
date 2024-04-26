from typing import Optional

from utils.ListNode import ListNode


def oddEvenList(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head or not head.next:
        return head

    odd_pointer = head
    even_pointer = head.next
    even_head = even_pointer

    while even_pointer and even_pointer.next:
        odd_pointer.next = even_pointer.next
        odd_pointer = odd_pointer.next
        even_pointer.next = odd_pointer.next
        even_pointer = even_pointer.next

    odd_pointer.next = even_head

    return head


if __name__ == '__main__':
    assert ListNode.from_list([1, 3, 5, 2, 4]) == oddEvenList(ListNode.from_list([1, 2, 3, 4, 5]))
    assert ListNode.from_list([2, 3, 6, 7, 1, 5, 4]) == oddEvenList(ListNode.from_list([2, 1, 3, 5, 6, 4, 7]))
