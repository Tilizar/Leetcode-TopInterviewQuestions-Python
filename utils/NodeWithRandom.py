class Node:
    def __init__(self, val=0, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random

    def __hash__(self):
        return hash(self.val) + hash(self.next)

    def __eq__(self, other):
        return (
            self.__class__ == other.__class__ and
            self.val == other.val and
            self.next == other.next
        )
