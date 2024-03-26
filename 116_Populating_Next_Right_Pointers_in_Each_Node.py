from typing import Optional

from utils.NodeWithLeftAndRight import Node


def connect(root: Optional[Node]) -> Optional[Node]:
    stack = []
    if root:
        stack.append(root)

    while stack:
        level = []
        for i in range(len(stack)):
            current = stack.pop(0)
            if current:
                level.append(current)
                stack.append(current.left)
                stack.append(current.right)
        if level:
            for i in range(len(level) - 1):
                level[i].next = level[i + 1]

    return root


def case_1():
    input_tree = Node(1, left=Node(2, left=Node(4), right=Node(5)), right=Node(3, left=Node(6), right=Node(7)))
    output = connect(input_tree)

    node_7 = Node(7)
    node_6 = Node(6, next=node_7)
    node_5 = Node(5, next=node_6)
    node_4 = Node(4, next=node_5)
    node_3 = Node(3, left=node_6, right=node_7)
    node_2 = Node(2, next=node_3, left=node_4, right=node_5)
    expected = Node(1, left=node_2, right=node_3)

    assert expected == output


def case_2():
    assert connect(None) is None


if __name__ == '__main__':
    case_1()
    case_2()
