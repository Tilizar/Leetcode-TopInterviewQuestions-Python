from typing import Optional

from utils.ListNode import ListNode


def hasCycle(head: Optional[ListNode]) -> bool:
    slow, fast = head, head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True

    return False


if __name__ == '__main__':
    first_last_cycle_node = ListNode(-4)
    first_first_cycle_node = ListNode(2, next=ListNode(0, next=first_last_cycle_node))
    first_last_cycle_node.next = first_first_cycle_node
    first_case_node = ListNode(3, next=first_first_cycle_node)
    assert hasCycle(first_case_node)

    second_last_cycle_node = ListNode(2)
    second_case_node = ListNode(1, next=second_last_cycle_node)
    second_last_cycle_node.next = second_case_node
    assert hasCycle(second_case_node)

    third_case_mode = ListNode(1)
    assert not hasCycle(third_case_mode)
