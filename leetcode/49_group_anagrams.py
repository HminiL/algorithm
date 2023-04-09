"""
https://leetcode.com/problems/group-anagrams/
49. Group Anagrams
Medium
"""
from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for string in strs:
            anagrams["".join(sorted(string))].append(string)
        return [x for x in anagrams.values()]

    def groupAnagrams2(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for string in strs:
            sorted_string = "".join(sorted(string))
            if sorted_string in anagrams.keys():
                anagrams[sorted_string].append(string)
            else:
                anagrams[sorted_string] = [string]
        return list(anagrams.values())
