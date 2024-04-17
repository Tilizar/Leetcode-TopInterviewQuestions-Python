from utils.ListNode import ListNode


def deleteNode(node: ListNode):
    node.val = node.next.val
    node.next = node.next.next


def case_1():
    linked_list = ListNode.from_list([4, 5, 1, 9])
    node_to_delete = linked_list.next  # 5

    deleteNode(node_to_delete)

    assert ListNode.from_list([4, 1, 9]) == linked_list


def case_2():
    linked_list = ListNode.from_list([4, 5, 1, 9])
    node_to_delete = linked_list.next.next  # 1

    deleteNode(node_to_delete)

    assert ListNode.from_list([4, 5, 9]) == linked_list


if __name__ == '__main__':
    case_1()
    case_2()
