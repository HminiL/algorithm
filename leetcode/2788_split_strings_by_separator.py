"""
https://leetcode.com/problems/split-strings-by-separator/description/
2788. Split Strings by Separator
Easy
Array
"""
from typing import List


class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        res = []
        for word in words:
            res.extend(word.split(separator))
        return res


def test_solution():
    solution = Solution()
    assert solution.splitWordsBySeparator(["hello world"], " ") == [
        "hello",
        "world",
    ], "error on test case 1"
    assert solution.splitWordsBySeparator(["hello world"], ",") == [
        "hello world",
    ], "error on test case 2"
    assert solution.splitWordsBySeparator(["hello,world"], ",") == [
        "hello",
        "world",
    ], "error on test case 3"


if __name__ == "__main__":
    test_solution()
