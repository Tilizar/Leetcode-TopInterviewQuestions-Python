from typing import List


def partition(s: str) -> List[List[str]]:
    output = []
    current_part = []

    def is_palindrome(start: int, end: int) -> bool:
        while start < end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True

    def dfs(start_index: int):
        if start_index == len(s):
            output.append(current_part.copy())
            return
        for i in range(start_index, len(s)):
            if is_palindrome(start_index, i):
                current_part.append(s[start_index:i + 1])
                dfs(i + 1)
                current_part.pop()

    dfs(0)
    return output


if __name__ == '__main__':
    assert [['a', 'a', 'b'], ['aa', 'b']] == partition('aab')
    assert [['a']] == partition('a')
