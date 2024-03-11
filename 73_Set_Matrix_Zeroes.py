from typing import List


def setZeroes(matrix: List[List[int]]) -> None:
    first_row_should_be_zero = False

    for row in range(len(matrix)):
        for column in range(len(matrix[0])):
            if (matrix[row][column]) == 0:
                matrix[0][column] = 0
                if row == 0:
                    first_row_should_be_zero = True
                else:
                    matrix[row][0] = 0

    for row in range(1, len(matrix)):
        for column in range(1, len(matrix[0])):
            if matrix[0][column] == 0 or matrix[row][0] == 0:
                matrix[row][column] = 0

    if matrix[0][0] == 0:
        for row in range(len(matrix)):
            matrix[row][0] = 0

    if first_row_should_be_zero:
        for column in range(len(matrix[0])):
            matrix[0][column] = 0


if __name__ == '__main__':
    first = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    setZeroes(first)
    assert [[1, 0, 1], [0, 0, 0], [1, 0, 1]] == first

    second = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
    setZeroes(second)
    assert [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]] == second
