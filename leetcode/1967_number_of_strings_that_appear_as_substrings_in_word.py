"""
https://leetcode.com/problems/number-of-strings-that-appear-as-substrings-in-word/description/
1967. Number of Strings That Appear as Substrings in Word
Easy
string
"""
from typing import List


class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        return sum([1 for pattern in patterns if pattern in word])


def test_solution():
    solution = Solution()
    case1 = solution.numOfStrings(["a", "abc", "bc", "d"], "abc")
    assert case1 == 3, f"error on test case 1: {case1}"
    case2 = solution.numOfStrings(["a", "b", "c"], "aaaaabbbbb")
    assert case2 == 2, f"error on test case 2: {case2}"
    case3 = solution.numOfStrings(["a", "a", "a"], "ab")
    assert case3 == 3, f"error on test case 3: {case3}"


if __name__ == "__main__":
    test_solution()
