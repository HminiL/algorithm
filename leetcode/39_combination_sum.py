"""
https://leetcode.com/problems/combination-sum/description/
39. Combination Sum
Array, dfs
"""
from typing import List


class Solution1:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(candidates, target, path, res):
            if target < 0:
                return
            if target == 0:
                res.append(path)
                return
            for i in range(len(candidates)):
                dfs(candidates[i:], target - candidates[i], path + [candidates[i]], res)

        res = []
        dfs(candidates, target, [], res)
        return res


def test_solution1():
    solution = Solution1()
    candidates1 = [2, 3, 6, 7]
    target1 = 7
    candidates2 = [2, 3, 5]
    target2 = 8
    assert solution.combinationSum(candidates1, target1) == [
        [2, 2, 3],
        [7],
    ], "error on test case1"
    assert solution.combinationSum(candidates2, target2) == [
        [2, 2, 2, 2],
        [2, 3, 3],
        [3, 5],
    ], "error on test case2"


if __name__ == "__main__":
    test_solution1()
