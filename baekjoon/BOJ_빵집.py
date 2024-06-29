# BOJ 3109 빵집
def get_input_data(input_file_path):
    f = open(input_file_path, "r")
    input = f.readline
    R, C = map(int, input().split())
    board = [list(input().strip()) for _ in range(R)]
    return R, C, board


def dfs(R, C, board, visited, x, y):
    if y == C - 1:
        return True
    for dx in [-1, 0, 1]:
        ax = x + dx
        ay = y + 1
        if 0 <= ax < R and 0 <= ay < C:
            if board[ax][ay] != "x" and visited[ax][ay] == -1:
                visited[ax][ay] = 1
                if dfs(R, C, board, visited, ax, ay):
                    return True
    return False


def solution(R, C, board):
    answer = 0
    visited = [[-1 for _ in range(C)] for _ in range(R)]
    for i in range(R):
        if dfs(R, C, board, visited, i, 0):
            answer += 1
    return answer


if __name__ == "__main__":
    input_data_1 = get_input_data("input_files/3109_input_1.txt")
    soulution_1 = solution(*input_data_1)
    assert soulution_1 == 2, f"Expected Result : 2, Returned Result : {soulution_1}"

    input_data_2 = get_input_data("input_files/3109_input_2.txt")
    soulution_2 = solution(*input_data_2)
    assert soulution_2 == 5, f"Expected Result : 5, Returned Result : {soulution_2}"
