class Node:
    def __init__(self):
        self.nodes = {}
        self.isEnd = False


class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        current = self.root
        for char in word:
            if char not in current.nodes:
                current.nodes[char] = Node()
            current = current.nodes[char]
        current.isEnd = True

    def search(self, word: str) -> bool:
        current = self.root
        for char in word:
            if char not in current.nodes:
                return False
            current = current.nodes[char]
        return current.isEnd

    def startsWith(self, prefix: str) -> bool:
        current = self.root
        for char in prefix:
            if char not in current.nodes:
                return False
            current = current.nodes[char]
        return True


if __name__ == '__main__':
    trie = Trie()
    trie.insert("apple")
    assert trie.search("apple")
    assert not trie.search("app")
    assert trie.startsWith("app")
    trie.insert("app")
    assert trie.search("app")
