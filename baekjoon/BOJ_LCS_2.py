# BOJ 9252 LCS 2
def get_input_data(file_path):
    f = open(file_path, "r")
    str1 = f.readline().strip()
    str2 = f.readline().strip()
    return str1, str2


def solution(str1, str2):
    dp = [[""] * (len(str2) + 1) for _ in range(len(str1) + 1)]
    for i in range(1, len(str1) + 1):
        for j in range(1, len(str2) + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + str1[i - 1]
            else:
                if len(dp[i - 1][j]) > len(dp[i][j - 1]):
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i][j - 1]
    return len(dp[-1][-1]), dp[-1][-1]


if __name__ == "__main__":
    input_data = get_input_data("input_files/9252_input.txt")
    sol = solution(*input_data)
    assert sol == (4, "ACAK"), f"Expected Result : (4, 'ACAK'), Returned Result : {sol}"
