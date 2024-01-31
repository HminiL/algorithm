"""
https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/description/
1700. Number of Students Unable to Eat Lunch
Easy
array
"""
from collections import Counter, deque
from typing import List


class Solution1:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        students = deque(students)
        sandwiches = deque(sandwiches)
        check = True
        idx = 0
        while check:
            check = False
            if len(sandwiches) != 0:
                idx = sandwiches[0]
            for i in range(len(students)):
                temp = students.popleft()
                if idx == temp:
                    sandwiches.popleft()
                    check = True
                    break
                else:
                    students.append(temp)
        return len(sandwiches)


class Solution2:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        counter = Counter(students)
        for sandwich in sandwiches:
            if counter[sandwich] == 0:
                break
            counter[sandwich] -= 1
        return sum(counter.values())


def test_solution1():
    solution = Solution1()
    case1 = solution.countStudents([1, 1, 0, 0], [0, 1, 0, 1])
    assert case1 == 0, f"error on test case 1-1: {case1}"
    case2 = solution.countStudents([1, 1, 1, 0, 0, 1], [1, 0, 0, 0, 1, 1])
    assert case2 == 3, f"error on test case 1-2: {case2}"


def test_solution2():
    solution = Solution2()
    case1 = solution.countStudents([1, 1, 0, 0], [0, 1, 0, 1])
    assert case1 == 0, f"error on test case 2-1: {case1}"
    case2 = solution.countStudents([1, 1, 1, 0, 0, 1], [1, 0, 0, 0, 1, 1])
    assert case2 == 3, f"error on test case 2-2: {case2}"


if __name__ == "__main__":
    test_solution1()
    test_solution2()
