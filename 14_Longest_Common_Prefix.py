from typing import List


def longestCommonPrefix(strs: List[str]) -> str:
    prefix = ""
    strs = sorted(strs)
    first = strs[0]
    last = strs[-1]

    for i in range(min(len(first), len(last))):
        if first[i] == last[i]:
            prefix += first[i]
        else:
            return prefix

    return prefix


if __name__ == '__main__':
    assert "fl" == longestCommonPrefix(["flower", "flow", "flight"])
    assert "" == longestCommonPrefix(["dog", "racecar", "car"])