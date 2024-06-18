"""
https://leetcode.com/problems/queue-reconstruction-by-height/description/
406. Queue Reconstruction by Height
Medium
Greedy
"""
import heapq
from typing import List


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        heap = []
        for person in people:
            heapq.heappush(heap, (-person[0], person[1]))
        result = []
        while heap:
            person = heapq.heappop(heap)
            result.insert(person[1], [-person[0], person[1]])
        return result


class Solution2:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x: (-x[0], x[1]))
        result = []
        for person in people:
            result.insert(person[1], [person[0], person[1]])
        return result


class InputValue:
    def case1(self):
        return [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]

    def case2(self):
        return [[6, 0], [5, 0], [4, 0], [3, 2], [2, 2], [1, 4]]


if __name__ == "__main__":
    iv = InputValue()
    s = Solution()
    assert s.reconstructQueue(iv.case1()) == [
        [5, 0],
        [7, 0],
        [5, 2],
        [6, 1],
        [4, 4],
        [7, 1],
    ], "Test Case 1 Failed"
    assert s.reconstructQueue(iv.case2()) == [
        [4, 0],
        [5, 0],
        [2, 2],
        [3, 2],
        [1, 4],
        [6, 0],
    ], "Test Case 2 Failed"

    s2 = Solution2()
    assert s2.reconstructQueue(iv.case1()) == [
        [5, 0],
        [7, 0],
        [5, 2],
        [6, 1],
        [4, 4],
        [7, 1],
    ], "Test Case 2-1 Failed"
    assert s2.reconstructQueue(iv.case2()) == [
        [4, 0],
        [5, 0],
        [2, 2],
        [3, 2],
        [1, 4],
        [6, 0],
    ], "Test Case 2-2 Failed"
