import heapq
from typing import List


def findKthLargest(nums: List[int], k: int) -> int:
    queue = []

    for num in nums:
        heapq.heappush(queue, num)
        if len(queue) > k:
            heapq.heappop(queue)

    return queue[0]


if __name__ == '__main__':
    assert 5 == findKthLargest([3, 2, 1, 5, 6, 4], 2)
    assert 4 == findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4)
