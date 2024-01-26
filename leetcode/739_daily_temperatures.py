"""
https://leetcode.com/problems/daily-temperatures/description/
739. Daily Temperatures
medium
stack
"""
from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for i, temperature in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temperature:
                j = stack.pop()
                res[j] = i - j
            stack.append(i)
        return res


def test_solution():
    solution = Solution()
    assert solution.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]) == [
        1,
        1,
        4,
        2,
        1,
        1,
        0,
        0,
    ], "error on test case 1"
    assert solution.dailyTemperatures([30, 40, 50, 60]) == [
        1,
        1,
        1,
        0,
    ], "error on test case 2"
    assert solution.dailyTemperatures([30, 60, 90]) == [1, 1, 0], "error on test case 3"


if __name__ == "__main__":
    test_solution()
