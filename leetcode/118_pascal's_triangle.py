"""
https://leetcode.com/problems/pascals-triangle/description/
118. Pascal's Triangle
Easy
Dynamic Programming
"""
from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        answer = []
        answer.append([1])

        for i in range(1, numRows):
            row = [1]
            for j in range(len(answer[i - 1]) - 1):
                row.append(answer[i - 1][j] + answer[i - 1][j + 1])
            row.append(1)
            answer.append(row)

        return answer


# Advanced solution
class Solution2:
    def generate(self, numRows):
        triangle = [[1]]

        for _ in range(1, numRows):
            prev_row = triangle[-1]
            new_row = [1]
            for i in range(1, len(prev_row)):
                new_row.append(prev_row[i - 1] + prev_row[i])
            new_row.append(1)
            triangle.append(new_row)
        return triangle


if __name__ == "__main__":
    s = Solution()
    assert s.generate(5) == [
        [1],
        [1, 1],
        [1, 2, 1],
        [1, 3, 3, 1],
        [1, 4, 6, 4, 1],
    ], s.generate(5)
    assert s.generate(1) == [[1]], s.generate(1)
    s2 = Solution2()
    assert s2.generate(5) == [
        [1],
        [1, 1],
        [1, 2, 1],
        [1, 3, 3, 1],
        [1, 4, 6, 4, 1],
    ], s2.generate(5)
    assert s2.generate(1) == [[1]], s2.generate(1)
