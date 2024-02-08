from collections import defaultdict


def isAnagram(s: str, t: str) -> bool:
    cache = defaultdict(int)

    for char in s:
        cache[char] += 1

    for char in t:
        cache[char] -= 1

    for count in cache.values():
        if count != 0:
            return False

    return True


if __name__ == '__main__':
    assert isAnagram('anagram', 'nagaram')
    assert not isAnagram('rat', 'car')
