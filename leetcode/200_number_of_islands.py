"""
200. Number of Islands
https://leetcode.com/problemset/all/?search=200&page=1
Medium
"""


from typing import List


# First
class Solution1:
    def numIslands(self, grid: List[List[str]]) -> int:
        need_visit = list()
        visited = list()
        count = 0
        for h in range(len(grid)):
            for v in range(len(grid[h])):
                if [h, v] in visited:
                    continue
                if grid[h][v] == "1":
                    need_visit.append([h, v])
                    count += 1
                else:
                    continue
                while need_visit:
                    land = need_visit.pop()
                    if land not in visited:
                        visited.append(land)
                        if land[1] + 1 < len(grid[h]) and grid[land[0]][land[1] + 1] == "1":
                            need_visit.append([land[0], land[1] + 1])
                        if land[0] + 1 < len(grid) and grid[land[0] + 1][land[1]] == "1":
                            need_visit.append([land[0] + 1, land[1]])
                        if land[1] - 1 >= 0 and grid[land[0]][land[1] - 1] == "1":
                            need_visit.append([land[0], land[1] - 1])
                        if land[0] - 1 >= 0 and grid[land[0] - 1][land[1]] == "1":
                            need_visit.append([land[0] - 1, land[1]])
        return count


class Solution2:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    count = self.dfs(i, j, grid, count)
        return count

    def dfs(self, x, y, grid, count):
        stack = [(x, y)]
        x_bound, y_bound = len(grid), len(grid[0])
        while stack:
            xx, yy = stack.pop()
            grid[xx][yy] = "2"
            for i, j in [[xx, yy+1], [xx+1, yy], [xx, yy-1], [xx-1, yy]]:
                if 0 <= i < x_bound and 0 <= j < y_bound and grid[i][j] == "1":
                    stack.append((i, j))
        return count+1





if __name__ == '__main__':
    # s = Solution1()
    # assert s.numIslands([
    #     ["1", "1", "1", "1", "0"],
    #     ["1", "1", "0", "1", "0"],
    #     ["1", "1", "0", "0", "0"],
    #     ["0", "0", "0", "0", "0"]
    # ]) == 1, \
    #     s.numIslands([
    #         ["1", "1", "1", "1", "0"],
    #         ["1", "1", "0", "1", "0"],
    #         ["1", "1", "0", "0", "0"],
    #         ["0", "0", "0", "0", "0"]
    #     ])

    s2 = Solution2()
    assert s2.numIslands([
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]) == 1, \
        s2.numIslands([
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"]
        ])
    assert s2.numIslands([["1", "1", "0", "0", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "1", "0", "0"],
                          ["0", "0", "0", "1", "1"]]) == 3, \
        s2.numIslands(
        [["1", "1", "0", "0", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "1", "0", "0"], ["0", "0", "0", "1", "1"]])
