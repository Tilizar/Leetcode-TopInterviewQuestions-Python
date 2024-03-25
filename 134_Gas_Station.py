from typing import List


def canCompleteCircuit(gas: List[int], cost: List[int]) -> int:
    if sum(gas) < sum(cost):
        return -1

    tank = 0
    found = 0

    for i in range(len(gas)):
        tank += gas[i] - cost[i]

        if tank < 0:
            tank = 0
            found = i + 1

    return found


if __name__ == '__main__':
    assert 3 == canCompleteCircuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2])
    assert -1 == canCompleteCircuit([2, 3, 4], [3, 4, 3])
