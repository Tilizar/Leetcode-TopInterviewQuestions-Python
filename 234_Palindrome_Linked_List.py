from typing import Optional

from utils.ListNode import ListNode


def isPalindrome(head: Optional[ListNode]) -> bool:
    slow, fast = head, head

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

    current = slow
    prev = None

    while current:
        next = current.next
        current.next = prev
        prev = current
        current = next

    left, right = head, prev

    while right:
        if left.val != right.val:
            return False
        left = left.next
        right = right.next

    return True


if __name__ == '__main__':
    assert isPalindrome(ListNode(1, next=ListNode(2, next=ListNode(2, next=ListNode(1)))))
    assert not isPalindrome(ListNode(1, next=ListNode(2)))
