"""
https://leetcode.com/problems/integer-to-roman/description/
12. Integer to Roman
medium
string
"""


class Solution:
    def intToRoman(self, num: int) -> str:
        int_to_roman_map = {
            1000: "M",
            900: "CM",
            500: "D",
            400: "CD",
            100: "C",
            90: "XC",
            50: "L",
            40: "XL",
            10: "X",
            9: "IX",
            5: "V",
            4: "IV",
            1: "I",
        }
        res = ""
        for k, v in int_to_roman_map.items():
            while num >= k:
                res += v
                num -= k
        return res


def test_solution():
    solution = Solution()
    assert solution.intToRoman(3) == "III", "error on test case 1"
    assert solution.intToRoman(4) == "IV", "error on test case 2"
    assert solution.intToRoman(9) == "IX", "error on test case 3"
    assert solution.intToRoman(58) == "LVIII", "error on test case 4"
    assert solution.intToRoman(1994) == "MCMXCIV", "error on test case 5"


if __name__ == "__main__":
    test_solution()
