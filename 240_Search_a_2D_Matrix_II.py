from typing import List


def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    row, column = 0, len(matrix[0]) - 1

    while column >= 0 and row <= len(matrix) - 1:
        if target < matrix[row][column]:
            column -= 1
        elif target > matrix[row][column]:
            row += 1
        else:
            return True

    return False


if __name__ == '__main__':
    matrix = [
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
    ]
    assert searchMatrix(matrix, 5)
    assert not searchMatrix(matrix, 20)
