def lengthOfLongestSubstring(s: str) -> int:
    cache = set()
    left = 0
    output = 0

    for right in range(len(s)):
        while s[right] in cache:
            cache.remove(s[left])
            left += 1
        cache.add(s[right])
        output = max(output, len(cache))

    return output


if __name__ == '__main__':
    assert 3 == lengthOfLongestSubstring('abcabcbb')
    assert 1 == lengthOfLongestSubstring('bbbbb')
    assert 3 == lengthOfLongestSubstring('pwwkew')
