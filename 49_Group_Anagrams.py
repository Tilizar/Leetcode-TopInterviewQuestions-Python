from collections import defaultdict
from typing import List


def groupAnagrams(strs: List[str]) -> List[List[str]]:
    cache = defaultdict(list)

    for word in strs:
        cache[str(sorted(word))].append(word)

    return list(cache.values())


if __name__ == '__main__':
    assert [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']] == groupAnagrams(['eat', 'tea', 'tan', 'ate', 'nat', 'bat'])
    assert [['']] == groupAnagrams([''])
    assert [['a']] == groupAnagrams(['a'])
