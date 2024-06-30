# BOJ 인구 이동 16234
from collections import deque


def get_input_data(file_path):
    f = open(file_path, "r")
    n, l, r = map(int, f.readline().split())
    graph = [list(map(int, f.readline().split())) for _ in range(n)]
    return n, l, r, graph


def bfs(n, l, r, graph, visited, x, y):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    queue = deque()
    queue.append((x, y))
    visited[x][y] = 1
    union = [(x, y)]

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
                if l <= abs(graph[nx][ny] - graph[x][y]) <= r:
                    queue.append((nx, ny))
                    visited[nx][ny] = 1
                    union.append((nx, ny))

    return union


def solution(n, l, r, graph) -> int:
    count = 0
    while True:
        visited = [[0] * n for _ in range(n)]
        flag = 0
        for i in range(n):
            for j in range(n):
                union = [(i, j)]
                if visited[i][j] == 0:
                    union = bfs(n, l, r, graph, visited, i, j)
                if len(union) > 1:
                    flag = 1
                    sum_population = sum(graph[x][y] for x, y in union) // len(union)
                    for x, y in union:
                        graph[x][y] = sum_population
        if flag == 0:
            break
        count += 1
    return count


if __name__ == "__main__":
    input_and_result = [
        ("input_files/16234_input_1.txt", 1),
        ("input_files/16234_input_2.txt", 0),
        ("input_files/16234_input_3.txt", 1),
        ("input_files/16234_input_4.txt", 2),
        ("input_files/16234_input_5.txt", 3),
    ]
    for file, result in input_and_result:
        n, l, r, graph = get_input_data(file)
        sol = solution(n, l, r, graph)
        assert (
            sol == result
        ), f"file_{file[-5]} Expected Result : {result}, Returned Result : {sol}"
