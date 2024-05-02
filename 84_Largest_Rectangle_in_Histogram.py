from typing import List


def largestRectangleArea(heights: List[int]) -> int:
    stack = []
    output = 0

    for i in range(len(heights)):
        height = heights[i]
        current_start_index = i
        while stack and stack[-1][1] > height:
            start_index, max_height = stack.pop()
            output = max(output, max_height * (i - start_index))
            current_start_index = start_index
        stack.append((current_start_index, height))

    for index, height in stack:
        output = max(output, height * (len(heights) - index))

    return output


if __name__ == '__main__':
    assert 10 == largestRectangleArea([2, 1, 5, 6, 2, 3])
    assert 4 == largestRectangleArea([2, 4])
