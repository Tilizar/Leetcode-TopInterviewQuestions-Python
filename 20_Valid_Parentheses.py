def isValid(s: str) -> bool:
        stack = []

        for char in s:
            if char == '(':
                stack.append(')')
            elif char == '[':
                stack.append(']')
            elif char == '{':
                stack.append('}')
            elif len(stack) == 0 or stack.pop() != char:
                return False

        return len(stack) == 0


if __name__ == '__main__':
    assert isValid("()")
    assert isValid("()[]{}")
    assert not isValid("(]")
