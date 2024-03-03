from typing import List


def rotate(matrix: List[List[int]]) -> None:
    top = 0
    bottom = len(matrix) - 1
    left = 0
    right = bottom

    while top < bottom and left < right:

        for offset in range(right - left):
            top_left = matrix[top][left + offset]
            top_right = matrix[top + offset][right]
            bottom_right = matrix[bottom][right - offset]
            bottom_left = matrix[bottom - offset][left]

            matrix[top][left + offset] = bottom_left
            matrix[top + offset][right] = top_left
            matrix[bottom][right - offset] = top_right
            matrix[bottom - offset][left] = bottom_right

        top += 1
        bottom -= 1
        left += 1
        right -= 1


if __name__ == '__main__':
    first = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    rotate(first)
    assert [[7, 4, 1], [8, 5, 2], [9, 6, 3]] == first

    second = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
    rotate(second)
    assert [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]] == second
