from collections import defaultdict, deque
from typing import List


def canFinish(numCourses: int, prerequisites: List[List[int]]) -> bool:
    cache = defaultdict(list)

    for course, pre_course in prerequisites:
        cache[course].append(pre_course)

    visited = set()
    checked = set()

    def dfs(course: int) -> bool:
        if course in visited:
            return False
        if course in checked or len(cache[course]) == 0:
            return True

        visited.add(course)

        for pre_course in cache[course]:
            if not dfs(pre_course):
                return False

        visited.remove(course)
        checked.add(course)
        return True

    for course in range(numCourses):
        if not dfs(course):
            return False
    return True


if __name__ == '__main__':
    assert canFinish(2, [[1, 0]])
    assert not canFinish(2, [[1, 0], [0, 1]])
    assert canFinish(5, [[1, 4], [2, 4], [3, 1], [3, 2]])
    assert canFinish(8, [[1, 0], [2, 6], [1, 7], [6, 4], [7, 0], [0, 5]])
