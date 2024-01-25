"""
https://leetcode.com/problems/sum-of-subarray-ranges/description/
2104. Sum of Subarray Ranges
Medium
array
"""
from typing import List


class Solution1:
    def subArrayRanges(self, nums: List[int]) -> int:
        res = 0
        for i in range(2, len(nums) + 1):
            k = 0
            while i + k <= len(nums):
                subarray = nums[k : k + i]
                min_value = min(subarray)
                max_value = max(subarray)
                res += max_value - min_value
                k += 1
        return res


class Solution2:
    def subArrayRanges(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)):
            min_value = nums[i]
            max_value = nums[i]
            for j in range(i, len(nums)):
                min_value = min(min_value, nums[j])
                max_value = max(max_value, nums[j])
                res += max_value - min_value
        return res


class Solution3:
    def subArrayRanges(self, nums: List[int]) -> int:
        n = len(nums)

        minsum = maxsum = 0
        stack = []
        for next_smaller in range(n + 1):
            while stack and (next_smaller == n or nums[stack[-1]] > nums[next_smaller]):
                i = stack.pop()
                prev_smaller = stack[-1] if stack else -1
                minsum += nums[i] * (next_smaller - i) * (i - prev_smaller)
            stack.append(next_smaller)
        stack = []
        for next_larger in range(n + 1):
            while stack and (next_larger == n or nums[stack[-1]] < nums[next_larger]):
                i = stack.pop()
                prev_larger = stack[-1] if stack else -1
                maxsum += nums[i] * (next_larger - i) * (i - prev_larger)
            stack.append(next_larger)

        return maxsum - minsum


def test_solution1():
    solution = Solution1()
    assert solution.subArrayRanges([1, 2, 3]) == 4, "error on test case 1-1"
    assert solution.subArrayRanges([1, 3, 3]) == 4, "error on test case 1-2"
    assert solution.subArrayRanges([4, -2, -3, 4, 1]) == 59, "error on test case 1-3"


def test_solution2():
    solution = Solution2()
    assert solution.subArrayRanges([1, 2, 3]) == 4, "error on test case 2-1"
    assert solution.subArrayRanges([1, 3, 3]) == 4, "error on test case 2-2"
    assert solution.subArrayRanges([4, -2, -3, 4, 1]) == 59, "error on test case 2-3"


def test_solution3():
    solution = Solution3()
    assert solution.subArrayRanges([1, 2, 3]) == 4, "error on test case 3-1"
    assert solution.subArrayRanges([1, 3, 3]) == 4, "error on test case 3-2"
    assert solution.subArrayRanges([4, -2, -3, 4, 1]) == 59, "error on test case 3-3"


if __name__ == "__main__":
    test_solution1()
    test_solution2()
    test_solution3()
