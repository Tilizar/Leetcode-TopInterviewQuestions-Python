from typing import List


def gameOfLife(board: List[List[int]]) -> None:
    new_life = set()

    def will_have_life(row, column) -> bool:
        current = board[row][column]

        row_last_index = len(board) - 1
        column_last_index = len(board[0]) - 1

        top = board[row - 1][column] if row > 0 else 0
        top_right = board[row - 1][column + 1] if row > 0 and column < column_last_index else 0
        right = board[row][column + 1] if column < column_last_index else 0
        bottom_right = board[row + 1][column + 1] if row < row_last_index and column < column_last_index else 0
        bottom = board[row + 1][column] if row < row_last_index else 0
        bottom_left = board[row + 1][column - 1] if row < row_last_index and column > 0 else 0
        left = board[row][column - 1] if column > 0 else 0
        top_left = board[row - 1][column - 1] if row > 0 and column > 0 else 0

        total = top + top_right + right + bottom_right + bottom + bottom_left + left + top_left

        return (total == 2 or total == 3) if current == 1 else total == 3

    for row in range(len(board)):
        for column in range(len(board[row])):
            if will_have_life(row, column):
                new_life.add((row, column))

    for row in range(len(board)):
        for column in range(len(board[row])):
            board[row][column] = 1 if (row, column) in new_life else 0


def case_1():
    input_board = [
        [0, 1, 0],
        [0, 0, 1],
        [1, 1, 1],
        [0, 0, 0]
    ]
    gameOfLife(input_board)
    expected = [
        [0, 0, 0],
        [1, 0, 1],
        [0, 1, 1],
        [0, 1, 0]
    ]
    assert expected == input_board


def case_2():
    input_board = [
        [1, 1],
        [1, 0]
    ]
    gameOfLife(input_board)
    expected = [
        [1, 1],
        [1, 1]
    ]
    assert expected == input_board


if __name__ == '__main__':
    case_1()
    case_2()
