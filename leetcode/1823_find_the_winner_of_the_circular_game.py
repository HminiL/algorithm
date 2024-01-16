"""
https://leetcode.com/problems/find-the-winner-of-the-circular-game/description/
1823. Find the Winner of the Circular Game
Medium
Queue
"""
import collections


class Solution1:
    def findTheWinner(self, n: int, k: int) -> int:
        queue = collections.deque(range(1, n + 1))
        while len(queue) > 1:
            count = k - 1
            while count:
                queue.append(queue.popleft())
                count -= 1
            queue.popleft()

        return queue[0]


class Solution2:
    def findTheWinner(self, n: int, k: int) -> int:
        queue = list(range(1, n + 1))
        while len(queue) > 1:
            for _ in range(k - 1):
                queue.append(queue.pop(0))
            queue.pop(0)
        return queue[0]


# top-down recursion: time Θ(n) space Θ(n)
class Solution3:
    def findTheWinner(self, n: int, k: int) -> int:
        if n == 1:
            return 1
        return (k + self.findTheWinner(n - 1, k) - 1) % n + 1


# bottom-up time Θ(n) space Θ(1)
class Solution4:
    def findTheWinner(self, n: int, k: int) -> int:
        p = 1
        for i in range(1, n):
            # here i represent number of alive people
            # p is f(i,'cac')
            p = (k + p - 1) % (i + 1) + 1
            # p is f(i+1, 'cac')
        return p


def test_solution1():
    solution = Solution1()
    assert solution.findTheWinner(5, 2) == 3, "error on test case 1-1"
    assert solution.findTheWinner(6, 5) == 1, "error on test case 1-2"
    assert solution.findTheWinner(1, 1) == 1, "error on test case 1-3"


def test_solution2():
    solution = Solution2()
    assert solution.findTheWinner(5, 2) == 3, "error on test case 2-1"
    assert solution.findTheWinner(6, 5) == 1, "error on test case 2-2"
    assert solution.findTheWinner(1, 1) == 1, "error on test case 2-3"


def test_solution3():
    solution = Solution3()
    assert solution.findTheWinner(5, 2) == 3, "error on test case 3-1"
    assert solution.findTheWinner(6, 5) == 1, "error on test case 3-2"
    assert solution.findTheWinner(1, 1) == 1, "error on test case 3-3"


def test_solution4():
    solution = Solution4()
    assert solution.findTheWinner(5, 2) == 3, "error on test case 4-1"
    assert solution.findTheWinner(6, 5) == 1, "error on test case 4-2"
    assert solution.findTheWinner(1, 1) == 1, "error on test case 4-3"


if __name__ == "__main__":
    test_solution1()
    test_solution2()
    test_solution3()
    test_solution4()
