from typing import List


def solve(board: List[List[str]]) -> None:
    should_not_be_captured = set()

    def dfs(row: int, column: int):
        if (row not in range(0, len(board)) or column not in range(0, len(board[row]))
                or board[row][column] == 'X' or (row, column) in should_not_be_captured):
            return
        should_not_be_captured.add((row, column))
        dfs(row - 1, column)
        dfs(row, column - 1)
        dfs(row, column + 1)
        dfs(row + 1, column)

    for row in range(len(board)):
        for column in range(len(board[row])):
            if (board[row][column] == 'O'
                    and (row == 0 or column == 0 or row == len(board) - 1 or column == len(board[row]) - 1)):
                dfs(row, column)

    for row in range(len(board)):
        for column in range(len(board[row])):
            if (row, column) not in should_not_be_captured:
                board[row][column] = 'X'

    return


def case_1():
    board = [
        ['X', 'X', 'X', 'X'],
        ['X', 'O', 'O', 'X'],
        ['X', 'X', 'O', 'X'],
        ['X', 'O', 'X', 'X']
    ]

    solve(board)

    expected = [
        ['X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'X'],
        ['X', 'O', 'X', 'X']
    ]

    assert expected == board


def case_2():
    board = [['X']]

    solve(board)

    assert [['X']] == board


if __name__ == '__main__':
    case_1()
    case_2()
