"""
https://leetcode.com/problems/merge-sorted-array/description/?envType=study-plan-v2&envId=top-interview-150
88. Merge Sorted Array
Easy
Array
"""
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        In this case, return value is just for testing purpose.
        Real function should not return anything.
        """
        if len(nums1) > m:
            del nums1[m:]
        if len(nums2) > n:
            del nums2[n:]
        nums1.extend(nums2)
        nums1.sort()
        return nums1


class Solution2:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        In this case, return value is just for testing purpose.
        Real function should not return anything.
        """
        for j in range(n):
            nums1[m + j] = nums2[j]
        nums1.sort()
        return nums1


# two pointers
class Solution3:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        In this case, return value is just for testing purpose.
        Real function should not return anything.
        """
        i = m - 1
        j = n - 1
        k = m + n - 1
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1


class InputValue:
    def case1(self):
        nums1 = [1, 2, 3, 0, 0, 0]
        m = 3
        nums2 = [2, 5, 6]
        n = 3
        return nums1, m, nums2, n

    def case2(self):
        nums1 = [1]
        m = 1
        nums2 = []
        n = 0
        return nums1, m, nums2, n

    def case3(self):
        nums1 = [0]
        m = 0
        nums2 = [1]
        n = 1
        return nums1, m, nums2, n


if __name__ == "__main__":
    iv = InputValue()

    s = Solution()
    assert s.merge(*iv.case1()) == [1, 2, 2, 3, 5, 6], "test case 1 failed"
    assert s.merge(*iv.case2()) == [1], "test case 2 failed"
    assert s.merge(*iv.case3()) == [1], "test case 3 failed"

    s2 = Solution2()
    assert s2.merge(*iv.case1()) == [1, 2, 2, 3, 5, 6], "test case 2-1 failed"
    assert s2.merge(*iv.case2()) == [1], "test case 2-2 failed"
    assert s2.merge(*iv.case3()) == [1], "test case 2-3 failed"

    s3 = Solution3()
    assert s3.merge(*iv.case1()) == [1, 2, 2, 3, 5, 6], "test case 3-1 failed"
    assert s3.merge(*iv.case2()) == [1], "test case 3-2 failed"
    assert s3.merge(*iv.case3()) == [1], "test case 3-3 failed"
