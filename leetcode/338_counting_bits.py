"""
https://leetcode.com/problems/counting-bits/description/
338. Counting Bits
easy
Dynamic Programming
"""
from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n + 1)
        for i in range(1, n + 1):
            ans[i] = ans[i >> 1] + (i & 1)
        return ans


if __name__ == "__main__":
    s = Solution()
    assert s.countBits(2) == [0, 1, 1], s.countBits(2)
    assert s.countBits(5) == [0, 1, 1, 2, 1, 2], s.countBits(5)
