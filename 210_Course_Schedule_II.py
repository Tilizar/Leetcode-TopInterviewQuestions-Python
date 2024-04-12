from collections import defaultdict
from typing import List


def findOrder(numCourses: int, prerequisites: List[List[int]]) -> List[int]:
    cache = defaultdict(list)

    for course, pre_course in prerequisites:
        cache[course].append(pre_course)

    in_progress = set()
    checked = set()
    output = []

    def dfs(course: int) -> bool:
        if course in in_progress:
            return False
        if course in checked:
            return True

        in_progress.add(course)

        for pre_course in cache[course]:
            if not dfs(pre_course):
                return False

        in_progress.remove(course)
        checked.add(course)
        output.append(course)
        return True

    for course in range(numCourses):
        if not dfs(course):
            return []
    return output


if __name__ == '__main__':
    assert [0, 1] == findOrder(2, [[1, 0]])
    assert [0, 1, 2, 3] == findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]])
