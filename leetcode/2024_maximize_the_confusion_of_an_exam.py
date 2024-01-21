"""
https://leetcode.com/problems/maximize-the-confusion-of-an-exam/description/
2024. Maximize the Confusion of an Exam
medium
string
"""


class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        def helper(answerKey, k, target):
            i = j = 0
            res = 0
            while j < len(answerKey):
                if answerKey[j] != target:
                    k -= 1
                while k < 0:
                    if answerKey[i] != target:
                        k += 1
                    i += 1
                res = max(res, j - i + 1)
                j += 1
            return res

        return max(helper(answerKey, k, "T"), helper(answerKey, k, "F"))


def test_solution():
    solution = Solution()
    assert solution.maxConsecutiveAnswers("TTFF", 2) == 4, "error on test case 1"
    assert solution.maxConsecutiveAnswers("TFFT", 1) == 3, "error on test case 2"
    assert solution.maxConsecutiveAnswers("TTFTTFTT", 1) == 5, "error on test case 3"


if __name__ == "__main__":
    test_solution()
