from typing import List


def exist(board: List[List[str]], word: str) -> bool:
    visited = []

    def dfs(row: int, column: int, letter_pos: int):
        if letter_pos == len(word):
            return True
        if (row < 0 or column < 0 or
                row >= len(board) or column >= len(board[0]) or
                board[row][column] != word[letter_pos] or (row, column) in visited):
            return False

        visited.append((row, column))

        output = (dfs(row - 1, column, letter_pos + 1) or
                  dfs(row, column - 1, letter_pos + 1) or
                  dfs(row, column + 1, letter_pos + 1) or
                  dfs(row + 1, column, letter_pos + 1))

        visited.pop()

        return output

    for row in range(len(board)):
        for column in range(len(board[0])):
            if board[row][column] == word[0] and dfs(row, column, 0):
                return True

    return False


if __name__ == '__main__':
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    assert exist(board, "ABCCED")
    assert exist(board, "SEE")
    assert not exist(board, "ABCB")
