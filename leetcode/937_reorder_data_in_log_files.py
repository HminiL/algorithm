"""
https://leetcode.com/problems/reorder-data-in-log-files/
937. Reorder Data in Log Files
Medium
"""
from typing import List


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digit_list = []
        string_list = []
        for log in logs:
            if log.split()[1].isdigit():
                digit_list.append(log)
            else:
                string_list.append(log)
        string_list = sorted(string_list, key=lambda x:(x.split()[1:], x.split()[0]))
        return string_list + digit_list