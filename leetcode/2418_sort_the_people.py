"""
https://leetcode.com/problems/sort-the-people/description/
2418. Sort the People
Easy
Hash Table
"""
from typing import List


class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        return [name for _, name in sorted(zip(heights, names), reverse=True)]


def test_solution():
    solution = Solution()
    assert solution.sortPeople(["Mary", "John", "Emma"], [180, 165, 170]) == [
        "Mary",
        "Emma",
        "John",
    ], "error on test case 1"
    assert solution.sortPeople(["Alice", "Bob", "Bob"], [155, 185, 150]) == [
        "Bob",
        "Alice",
        "Bob",
    ], "error on test case 2"


if __name__ == "__main__":
    test_solution()
