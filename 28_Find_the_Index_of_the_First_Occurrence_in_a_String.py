def strStr(haystack: str, needle: str) -> int:
    for i in range(0, len(haystack) - len(needle) + 1):
        if haystack[i:(i+len(needle))] == needle:
            return i
    return -1


if __name__ == '__main__':
    assert 0 == strStr("sadbutsad", "sad")
    assert -1 == strStr("leetcode", "leeto")
    assert 2 == strStr("hello", "ll")
    assert 0 == strStr("a", "a")
