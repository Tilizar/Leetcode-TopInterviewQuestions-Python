from typing import List


def numIslands(grid: List[List[str]]) -> int:
    marked = set()

    def dfs(row: int, column: int):
        if (row not in range(len(grid)) or column not in range(len(grid[row]))
                or grid[row][column] == '0' or (row, column) in marked):
            return
        marked.add((row, column))
        dfs(row - 1, column)
        dfs(row, column - 1)
        dfs(row, column + 1)
        dfs(row + 1, column)

    output = 0

    for row in range(len(grid)):
        for column in range(len(grid[row])):
            if grid[row][column] == '1' and (row, column) not in marked:
                dfs(row, column)
                output += 1

    return output


if __name__ == '__main__':
    first = [
        ['1', '1', '1', '1', '0'],
        ['1', '1', '0', '1', '0'],
        ['1', '1', '0', '0', '0'],
        ['0', '0', '0', '0', '0']
    ]
    assert 1 == numIslands(first)

    second = [
        ['1', '1', '0', '0', '0'],
        ['1', '1', '0', '0', '0'],
        ['0', '0', '1', '0', '0'],
        ['0', '0', '0', '1', '1']
    ]
    assert 3 == numIslands(second)
