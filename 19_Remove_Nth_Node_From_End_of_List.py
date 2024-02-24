from typing import Optional

from utils.ListNode import ListNode


def removeNthFromEnd(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    cursor, before_found = head, head
    counter = 0

    while cursor:
        if counter <= n:
            counter += 1
        else:
            before_found = before_found.next
        cursor = cursor.next

    if counter == n:
        return head.next

    before_found.next = before_found.next.next

    return head


if __name__ == '__main__':
    assert ListNode.from_list([1, 2, 3, 5]) == removeNthFromEnd(ListNode.from_list([1, 2, 3, 4, 5]), 2)
    assert ListNode.from_list([]) == removeNthFromEnd(ListNode.from_list([1]), 1)
    assert ListNode.from_list([1]) == removeNthFromEnd(ListNode.from_list([1, 2]), 1)
