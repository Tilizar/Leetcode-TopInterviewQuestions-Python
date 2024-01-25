from typing import List


def generate(numRows: int) -> List[List[int]]:
    output = [[1]]

    for i in range(numRows - 1):
        prev = output[-1]
        new_row = [1]

        for j in range(1, len(prev)):
            new_row.append(prev[j - 1] + prev[j])

        new_row.append(1)

        output.append(new_row)

    return output


if __name__ == '__main__':
    expected = [
        [1],
        [1, 1],
        [1, 2, 1],
        [1, 3, 3, 1],
        [1, 4, 6, 4, 1]
    ]
    assert expected == generate(5)

    assert [[1]] == generate(1)
