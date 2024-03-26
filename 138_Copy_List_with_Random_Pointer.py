from typing import Optional

from utils.NodeWithRandom import Node


def copyRandomList(head: Optional[Node]) -> Optional[Node]:
    cache = dict()

    current = head
    while current:
        cache[current] = Node(current.val)
        current = current.next

    current = head
    while current:
        copy = cache[current]
        copy.next = cache.get(current.next)
        copy.random = cache.get(current.random)
        current = current.next

    return cache.get(head)


def case_1():
    fifth = Node(1, next=None)
    fourth = Node(10, next=fifth)
    third = Node(11, next=fourth)
    second = Node(13, next=third)
    first = Node(7, next=second)

    first.random = None
    second.random = first
    third.random = fifth
    fourth.random = third
    fifth.random = first

    output = copyRandomList(first)

    assert first is not output
    assert first == output


def case_2():
    second = Node(2, next=None)
    first = Node(1, next=second)

    first.random = second
    second.random = second

    output = copyRandomList(first)

    assert first is not output
    assert first == output


def case_3():
    third = Node(3, next=None)
    second = Node(3, next=third)
    first = Node(3, next=second)

    first.random = None
    second.random = first
    third.random = None

    output = copyRandomList(first)

    assert first is not output
    assert first == output


if __name__ == '__main__':
    case_1()
    case_2()
    case_3()
