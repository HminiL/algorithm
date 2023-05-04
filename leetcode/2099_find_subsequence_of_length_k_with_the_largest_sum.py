"""
https://leetcode.com/problems/find-subsequence-of-length-k-with-the-largest-sum/
2099. Find Subsequence of Length K With Maximum Sum
Easy
"""
from heapq import heappushpop, heappush
from typing import List


class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        num_with_idx = [[i, x] for i, x in enumerate(nums)]
        sorted_num = sorted(num_with_idx[-k:], key=lambda x: x[0])
        answer = [x[1] for x in sorted_num]
        return answer


class Solution2:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        res = []
        for i, n in enumerate(nums):
            if len(res) == k:
                heappushpop(res, (n, i))
            else:
                heappush(res, (n, i))
        return [x[0] for x in sorted(res, key=lambda x: x[1])]


if __name__ == '__main__':
    # print(Solution().maxSubsequence([18,3,19,-8,30,22,-35,11,16,18,-21,32,-7,-6,38,25,-21,-1,26,-8,-37,-39,-34,6,-36,-3,26,-32,22,-20,35,-35,-30,-8,11,7,-23,-9,-22,1,33,-6,12,2,27,-27,28,-12,21,12,16,21,33], 50))
    print(Solution2().maxSubsequence(
        [18, 3, 19, -8, 30, 22, -35, 11, 16, 18, -21, 32, -7, -6, 38, 25, -21, -1, 26, -8, -37, -39, -34, 6, -36, -3,
         26, -32, 22, -20, 35, -35, -30, -8, 11, 7, -23, -9, -22, 1, 33, -6, 12, 2, 27, -27, 28, -12, 21, 12, 16, 21,
         33], 50))
