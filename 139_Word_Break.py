from typing import List


def wordBreak(s: str, wordDict: List[str]) -> bool:
    can_reach_end_from = set()

    for i in range(len(s) - 1, -1, -1):
        for word in wordDict:
            next_start_index = i + len(word)
            if next_start_index > len(s):
                continue
            if s[i: next_start_index] == word:
                if next_start_index in can_reach_end_from or next_start_index == len(s):
                    can_reach_end_from.add(i)

    return 0 in can_reach_end_from


if __name__ == '__main__':
    assert wordBreak('leetcode', ['leet', 'code'])
    assert wordBreak('applepenapple', ['apple', 'pen'])
    assert not wordBreak('catsandog', ['cats', 'dog', 'sand', 'and', 'cat'])
