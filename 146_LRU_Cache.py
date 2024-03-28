class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.internal_map = {}
        self.key_stack = []

    def get(self, key: int) -> int:
        value = self.internal_map.get(key)
        if value is None:
            return -1
        self.key_stack.remove(key)
        self.key_stack.append(key)
        return value

    def put(self, key: int, value: int) -> None:
        if key in self.key_stack:
            self.key_stack.remove(key)
            self.internal_map.pop(key)

        if len(self.key_stack) == self.capacity:
            self.internal_map.pop(self.key_stack.pop(0))

        self.internal_map[key] = value
        self.key_stack.append(key)


if __name__ == '__main__':
    lru_cache = LRUCache(2)
    lru_cache.put(1, 1)
    lru_cache.put(2, 2)
    assert 1, lru_cache.get(1)
    lru_cache.put(3, 3)
    assert -1, lru_cache.get(2)
    lru_cache.put(4, 4)
    assert -1, lru_cache.get(1)
    assert 3, lru_cache.get(3)
    assert 4, lru_cache.get(4)
