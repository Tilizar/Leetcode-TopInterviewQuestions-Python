class Node:
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

    def __hash__(self):
        return hash(self.val) + hash(self.left) + hash(self.right) + hash(self.next)

    def __eq__(self, other):
        return (
            self.__class__ == other.__class__ and
            self.val == other.val and
            self.left == other.left and
            self.right == other.right and
            self.next == other.next
        )
