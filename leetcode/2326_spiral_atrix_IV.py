"""
https://leetcode.com/problems/spiral-matrix-iv/description/
2326. Spiral Matrix IV
medium
linked list
"""
from typing import Optional, List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution1:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        ans = [[-1] * n for _ in range(m)]
        i = j = p = 0
        dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        while 1:
            ans[i][j] = head.val
            head = head.next
            if not head:
                break
            while 1:
                x, y = i + dirs[p][0], j + dirs[p][1]
                if x < 0 or y < 0 or x >= m or y >= n or ~ans[x][y]:
                    p = (p + 1) % 4
                else:
                    i, j = x, y
                    break
        return ans


class Solution2:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        ans = [[-1] * (n) for _ in range(m)]
        first_row = 0
        first_col = 0
        last_row = m - 1
        last_col = n - 1
        while first_row < last_row and first_col < last_col:
            for j in range(first_col, last_col):
                ans[first_row][j] = head.val
                head = head.next
                if head is None:
                    return ans

            for i in range(first_row, last_row):
                ans[i][last_col] = head.val
                head = head.next
                if head is None:
                    return ans
            for j in range(last_col, first_col, -1):
                ans[last_row][j] = head.val
                head = head.next
                if head is None:
                    return ans
            for i in range(last_row, first_row, -1):
                ans[i][first_col] = head.val
                head = head.next
                if head is None:
                    return ans
            first_row += 1
            first_col += 1
            last_row -= 1
            last_col -= 1

        if head is None:
            for i in range(first_row, last_row + 1):
                for j in range(first_col, last_col + 1):
                    ans[i][j] = head.val
                    head = head.next
                    if head is None:
                        return ans
        return ans


def test_solution1():
    solution = Solution1()
    head1 = ListNode(
        3,
        ListNode(
            0,
            ListNode(
                2,
                ListNode(
                    6,
                    ListNode(
                        8,
                        ListNode(
                            1,
                            ListNode(
                                7,
                                ListNode(
                                    9,
                                    ListNode(
                                        4,
                                        ListNode(
                                            2, ListNode(5, ListNode(5, ListNode(0)))
                                        ),
                                    ),
                                ),
                            ),
                        ),
                    ),
                ),
            ),
        ),
    )
    assert solution.spiralMatrix(3, 4, head1) == [
        [3, 0, 2, 6, 8],
        [5, 0, -1, -1, 1],
        [5, 2, 4, 9, 7],
    ], "error on test case1"
    head2 = ListNode(0, ListNode(1, ListNode(2)))
    assert solution.spiralMatrix(1, 4, head2) == [[0, 1, 2, -1]], "error on test case2"


def test_solution2():
    solution = Solution2()
    [3, 0, 2, 6, 8, 1, 7, 9, 4, 2, 5, 5, 0]
    head1 = ListNode(
        3,
        ListNode(
            0,
            ListNode(
                2,
                ListNode(
                    6,
                    ListNode(
                        8,
                        ListNode(
                            1,
                            ListNode(
                                7,
                                ListNode(
                                    9,
                                    ListNode(
                                        4,
                                        ListNode(
                                            2, ListNode(5, ListNode(5, ListNode(0)))
                                        ),
                                    ),
                                ),
                            ),
                        ),
                    ),
                ),
            ),
        ),
    )
    assert solution.spiralMatrix(3, 4, head1) == [
        [3, 0, 2, 6, 8],
        [5, 0, -1, -1, 1],
        [5, 2, 4, 9, 7],
    ], "error on test case1"
    head2 = ListNode(0, ListNode(1, ListNode(2)))
    assert solution.spiralMatrix(1, 4, head2) == [[0, 1, 2, -1]], "error on test case2"


if __name__ == "__main__":
    # test_solution1()
    test_solution2()
