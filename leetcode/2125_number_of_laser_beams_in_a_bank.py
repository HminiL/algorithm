"""
https://leetcode.com/problems/number-of-laser-beams-in-a-bank/description/
2125. Number of Laser Beams in a Bank
Medium
string
"""
from typing import List


class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        ans = 0
        prevOnes = 0

        for row in bank:
            ones = row.count("1")
            if ones:
                ans += prevOnes * ones
                prevOnes = ones

        return ans


def test_solution():
    solution = Solution()
    case1 = solution.numberOfBeams(["011001", "000000", "010100", "001000"])
    assert case1 == 8, f"error on test case 1: {case1}"
    case2 = solution.numberOfBeams(["000", "111", "000"])
    assert case2 == 0, f"error on test case 2: {case2}"


if __name__ == "__main__":
    test_solution()
