"""
https://leetcode.com/problems/word-pattern/description/
290. Word Pattern
Easy
hash table
"""


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern) != len(words):
            return False
        d = {}
        for i in range(len(pattern)):
            if pattern[i] not in d:
                if words[i] in d.values():
                    return False
                d[pattern[i]] = words[i]
            else:
                if d[pattern[i]] != words[i]:
                    return False
        return True


def test_solution():
    solution = Solution()
    assert (
        solution.wordPattern("abba", "dog cat cat dog") is True
    ), "error on test case 1"
    assert (
        solution.wordPattern("abba", "dog cat cat fish") is False
    ), "error on test case 2"
    assert (
        solution.wordPattern("aaaa", "dog cat cat dog") is False
    ), "error on test case 3"
    assert (
        solution.wordPattern("abba", "dog dog dog dog") is False
    ), "error on test case 4"


if __name__ == "__main__":
    test_solution()
