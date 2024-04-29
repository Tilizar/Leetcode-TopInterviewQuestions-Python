from typing import List, Optional

from utils.ListNode import ListNode


def mergeKLists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    dummy = ListNode(-1)
    pointer = dummy

    while True:
        smallest = float('inf')
        smallest_index = -1

        for index, node in enumerate(lists):
            if node is not None:
                if smallest > node.val:
                    smallest = node.val
                    smallest_index = index

        if smallest_index == -1:
            break

        pointer.next = lists[smallest_index]
        lists[smallest_index] = lists[smallest_index].next
        pointer = pointer.next
        pointer.next = None

    return dummy.next


if __name__ == '__main__':
    lists = [
        ListNode.from_list([1, 4, 5]),
        ListNode.from_list([1, 3, 4]),
        ListNode.from_list([2, 6])
    ]
    assert ListNode.from_list([1, 1, 2, 3, 4, 4, 5, 6]) == mergeKLists(lists)
    assert mergeKLists([]) is None
    assert mergeKLists([None]) is None
