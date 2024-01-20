"""
27. Remove Element
"""
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        for i in range(nums.count(val)):
            nums.remove(val)
        return len(nums)


def test_solution1():
    solution = Solution()
    assert solution.removeElement([3, 2, 2, 3], 3) == 2, "error on test case 1"
    assert (
        solution.removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2) == 5
    ), "error on test case 2"


if __name__ == "__main__":
    test_solution1()
