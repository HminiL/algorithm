"""
https://leetcode.com/problems/finding-the-users-active-minutes/description/
1817. Finding the Users Active Minutes
medium
hash table
"""
from typing import List


class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        res = [0] * k
        table = {}
        for id, minute in logs:
            if id not in table:
                table[id] = set()
            table[id].add(minute)
        for id, minutes in table.items():
            res[len(minutes) - 1] += 1
        return res


def test_solution():
    solution = Solution()
    assert solution.findingUsersActiveMinutes(
        [[0, 5], [1, 2], [0, 2], [0, 5], [1, 3]], 5
    ) == [0, 2, 0, 0, 0], "error on test case 1"
    assert solution.findingUsersActiveMinutes([[1, 1], [2, 2], [2, 3]], 4) == [
        1,
        1,
        0,
        0,
    ], "error on test case 2"


if __name__ == "__main__":
    test_solution()
