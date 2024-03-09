from typing import List


def merge(intervals: List[List[int]]) -> List[List[int]]:
    intervals.sort(key=lambda x: x[0])
    output = []
    prev_left, prev_right = intervals[0][0], intervals[0][1]

    for left, right in intervals[1:]:
        if left <= prev_right:
            prev_right = max(right, prev_right)
        else:
            output.append([prev_left, prev_right])
            prev_left = left
            prev_right = right

    output.append([prev_left, prev_right])

    return output


if __name__ == '__main__':
    assert [[1, 6], [8, 10], [15, 18]] == merge([[1, 3], [2, 6], [8, 10], [15, 18]])
    assert [[1, 5]] == merge([[1, 4], [4, 5]])
    assert [[0, 4]] == merge([[1, 4], [0, 4]])
    assert [[1, 4]] == merge([[1, 4], [2, 3]])
