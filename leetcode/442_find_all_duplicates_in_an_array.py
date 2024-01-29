"""
https://leetcode.com/problems/find-all-duplicates-in-an-array/description/
442. Find All Duplicates in an Array
Medium
hash table
"""
from collections import defaultdict, Counter
from typing import List


class Solution1:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        int_count = defaultdict(int)
        res = []
        for num in nums:
            int_count[num] += 1
        for key, value in int_count.items():
            if value > 1:
                res.append(key)
        return sorted(res)


class Solution2:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        int_count = Counter(nums)
        res = []
        for key, value in int_count.items():
            if value > 1:
                res.append(key)
        return sorted(res)


class Solution3:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        for i in nums:
            if nums[abs(i) - 1] < 0:
                res.append(abs(i))
            nums[abs(i) - 1] *= -1
        return res


def test_solution1():
    solution = Solution1()
    assert solution.findDuplicates([4, 3, 2, 7, 8, 2, 3, 1]) == [
        2,
        3,
    ], "error on test case 1-1"
    assert solution.findDuplicates([1, 1, 2]) == [1], "error on test case 1-2"


def test_solution2():
    solution = Solution2()
    assert solution.findDuplicates([4, 3, 2, 7, 8, 2, 3, 1]) == [
        2,
        3,
    ], "error on test case 2-1"
    assert solution.findDuplicates([1, 1, 2]) == [1], "error on test case 2-2"


def test_solution3():
    solution = Solution3()
    assert solution.findDuplicates([4, 3, 2, 7, 8, 2, 3, 1]) == [
        2,
        3,
    ], "error on test case 3-1"
    assert solution.findDuplicates([1, 1, 2]) == [1], "error on test case 3-2"


if __name__ == "__main__":
    test_solution1()
    test_solution2()
    test_solution3()
