"""
https://leetcode.com/problems/fibonacci-number/description/
509. Fibonacci Number
easy
Dynamic Programming
"""


class Solution:
    def fib(self, n: int) -> int:
        cache = [0] * 31
        cache[0] = 0
        if n == 0:
            return cache[n]
        cache[1] = 1
        for i in range(2, n + 1):
            cache[i] = cache[i - 1] + cache[i - 2]
        return cache[n]


# Advanced solution
class Solution2:
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        dp = [0] * (n + 1)
        dp[0] = 0
        dp[1] = 1
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]


class Solution3:
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        prev2 = 0
        prev1 = 1
        curr = 0

        for _ in range(2, n + 1):
            curr = prev1 + prev2
            prev2, prev1 = prev1, curr
        return curr


if __name__ == "__main__":
    s = Solution()
    assert s.fib(2) == 1, s.fib(1)
    assert s.fib(3) == 2, s.fib(3)
    assert s.fib(4) == 3, s.fib(4)
    s2 = Solution2()
    assert s2.fib(2) == 1, s2.fib(1)
    assert s2.fib(3) == 2, s2.fib(3)
    assert s2.fib(4) == 3, s2.fib(4)
    s3 = Solution3()
    assert s3.fib(2) == 1, s3.fib(1)
    assert s3.fib(3) == 2, s3.fib(3)
    assert s3.fib(4) == 3, s3.fib(4)
