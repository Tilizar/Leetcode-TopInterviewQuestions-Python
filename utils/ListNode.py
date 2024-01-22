from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __hash__(self):
        return hash(self.val) + hash(self.next)

    def __eq__(self, other):
        return (
            self.__class__ == other.__class__ and
            self.val == other.val and
            self.next == other.next
        )

    @classmethod
    def from_list(cls, nums: List[int]):
        dummy = ListNode(-1)
        pointer = dummy
        for num in nums:
            pointer.next = ListNode(num)
            pointer = pointer.next
        return dummy.next

