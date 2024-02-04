"""
https://leetcode.com/problems/sort-the-students-by-their-kth-score/description/
2545. Sort the Students by Their Kth Score
Medium
Array
"""
from typing import List


class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        return sorted(score, key=lambda x: x[k], reverse=True)


def test_solution():
    solution = Solution()
    case1 = solution.sortTheStudents([[10, 6, 9, 1], [7, 5, 11, 2], [4, 8, 3, 15]], 2)
    assert case1 == [
        [7, 5, 11, 2],
        [10, 6, 9, 1],
        [4, 8, 3, 15],
    ], f"error on test case 1: {case1}"
    case2 = solution.sortTheStudents([[3, 4], [5, 6]], 0)
    assert case2 == [[5, 6], [3, 4]], f"error on test case 2: {case2}"


if __name__ == "__main__":
    test_solution()
