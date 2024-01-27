def isPalindrome(s: str) -> bool:
    chars = []

    for c in s:
        if c.isalpha() or c.isdigit():
            chars.append(c.lower())

    left, right = 0, len(chars) - 1

    while left < right:
        if chars[left] != chars[right]:
            return False
        left, right = left + 1, right - 1

    return True


if __name__ == '__main__':
    assert isPalindrome("A man, a plan, a canal: Panama")
    assert not isPalindrome("race a car")
    assert isPalindrome(" ")
    assert not isPalindrome("0P")
