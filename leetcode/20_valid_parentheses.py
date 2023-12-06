"""
https://leetcode.com/problems/valid-parentheses/
20. Valid Parentheses
Easy
"""


class Solution:
    def isValid(self, s: str) -> bool:
        start_bracket = ["(", "[", "{"]
        valid_list = []
        for x in s:
            if x in start_bracket:
                valid_list.append(x)
            else:
                if not valid_list:
                    return False
                elif valid_list[-1] == "(" and x == ")":
                    valid_list.pop()
                elif valid_list[-1] == "{" and x == "}":
                    valid_list.pop()
                elif valid_list[-1] == "[" and x == "]":
                    valid_list.pop()
                else:
                    return False
        return True if not valid_list else False


class Solution2:
    def isValid(self, s: str) -> bool:
        d = {"(": ")", "{": "}", "[": "]"}
        stack = []
        for i in s:
            if i in d:
                stack.append(i)
            elif not stack or d[stack.pop()] != i:
                return False
        return not stack


if __name__ == "__main__":
    print(Solution().isValid("["))
    print(Solution2().isValid("["))
