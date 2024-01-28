"""
https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to/description/
1282. Group the People Given the Group Size They Belong To
Medium
hash table
"""
from typing import List


class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        res = []
        table = {}
        for i, size in enumerate(groupSizes):
            if size not in table:
                table[size] = [[]]
            if len(table[size][-1]) == size:
                table[size].append([])
            table[size][-1].append(i)
        for size, groups in sorted(table.items()):
            res.extend(groups)
        return res


def test_solution():
    solution = Solution()
    assert solution.groupThePeople([3, 3, 3, 3, 3, 1, 3]) == [
        [5],
        [0, 1, 2],
        [3, 4, 6],
    ], "error on test case 1"
    assert solution.groupThePeople([2, 1, 3, 3, 3, 2]) == [
        [1],
        [0, 5],
        [2, 3, 4],
    ], "error on test case 2"


if __name__ == "__main__":
    test_solution()
