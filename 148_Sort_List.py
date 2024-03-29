from typing import Optional

from utils.ListNode import ListNode


def sortList(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head or not head.next:
        return head

    mid = find_mid(head)
    left = head
    right = mid.next
    mid.next = None

    left = sortList(left)
    right = sortList(right)

    return merge(left, right)


def find_mid(node: ListNode) -> ListNode:
    slow = node
    fast = node.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow


def merge(left: ListNode, right: ListNode) -> ListNode:
    dummy = ListNode(0)
    output = dummy

    while left and right:
        if left.val > right.val:
            output.next = right
            right = right.next
        else:
            output.next = left
            left = left.next
        output = output.next

    output.next = left if left else right

    return dummy.next


if __name__ == '__main__':
    assert ListNode.from_list([1, 2, 3, 4]) == sortList(ListNode.from_list([4, 2, 1, 3]))
    assert ListNode.from_list([-1, 0, 3, 4, 5]) == sortList(ListNode.from_list([-1, 5, 3, 4, 0]))
    assert sortList(None) is None
