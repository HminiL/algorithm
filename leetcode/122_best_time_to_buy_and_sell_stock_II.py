"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/
122. Best Time to Buy and Sell Stock II
Medium
Greedy
"""
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        for i in range(len(prices) - 1):
            if prices[i + 1] > prices[i]:
                result += prices[i + 1] - prices[i]
        return result


class InputValue:
    def case1(self):
        return [7, 1, 5, 3, 6, 4]

    def case2(self):
        return [1, 2, 3, 4, 5]

    def case3(self):
        return [7, 6, 4, 3, 1]


if __name__ == "__main__":
    iv = InputValue()
    s = Solution()
    assert s.maxProfit(iv.case1()) == 7, "Test Case 1 Failed"
    assert s.maxProfit(iv.case2()) == 4, "Test Case 2 Failed"
    assert s.maxProfit(iv.case3()) == 0, "Test Case 3 Failed"
