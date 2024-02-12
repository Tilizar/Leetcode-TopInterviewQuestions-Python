from typing import List


def reveseString(s: List[str]):
    left, right = 0, len(s) - 1
    while left < right:
        tmp = s[right]
        s[right] = s[left]
        s[left] = tmp

        left += 1
        right -= 1

    return


if __name__ == '__main__':
    first = ['h', 'e', 'l', 'l', 'o']
    reveseString(first)
    assert ['o', 'l', 'l', 'e', 'h'] == first

    second = ['H','a','n','n','a','h']
    reveseString(second)
    assert ['h','a','n','n','a','H'] == second
