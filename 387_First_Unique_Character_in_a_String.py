from collections import defaultdict


def firstUniqChar(s: str) -> int:
    cache = defaultdict(int)

    for c in s:
        cache[c] += 1

    for i, c in enumerate(s):
        if cache[c] == 1:
            return i

    return -1


if __name__ == '__main__':
    assert 0 == firstUniqChar('leetcode')
    assert 2 == firstUniqChar('loveleetcode')
    assert -1 == firstUniqChar('aabb')
