def longestPalindrome(s: str) -> str:
    palindrome = ''

    def find_palindrome(start, end) -> str:
        while start >= 0 and end < len(s) and s[start] == s[end]:
            start -= 1
            end += 1
        return s[start + 1:end]

    for i in range(len(s)):
        odd = find_palindrome(i, i)
        if len(odd) > len(palindrome):
            palindrome = odd

        even = find_palindrome(i, i + 1)
        if len(even) > len(palindrome):
            palindrome = even

    return palindrome


if __name__ == '__main__':
    assert 'bab' == longestPalindrome('babad')
    assert 'bb' == longestPalindrome('cbbd')
