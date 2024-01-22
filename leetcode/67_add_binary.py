"""
https://leetcode.com/problems/add-binary/description/
67. Add Binary
Easy
"""


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = []
        carry = 0
        i, j = len(a) - 1, len(b) - 1
        while i >= 0 or j >= 0 or carry:
            if i >= 0:
                carry += int(a[i])
                i -= 1
            if j >= 0:
                carry += int(b[j])
                j -= 1
            res.append(str(carry % 2))
            carry //= 2
        return "".join(res[::-1])


def test_solution():
    solution = Solution()
    assert solution.addBinary("11", "1") == "100", "error on test case 1"
    assert solution.addBinary("1010", "1011") == "10101", "error on test case 2"


if __name__ == "__main__":
    test_solution()
