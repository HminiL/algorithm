"""
2×n 타일링

문제
2×n 크기의 직사각형을 1×2, 2×1 타일로 채우는 방법의 수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 n이 주어진다. (1 ≤ n ≤ 1,000)

출력
첫째 줄에 2×n 크기의 직사각형을 채우는 방법의 수를 10,007로 나눈 나머지를 출력한다.
"""


def solution(n):
    cache = [0] * (n + 1)
    cache[1] = 1
    cache[2] = 2

    for i in range(3, n + 1):
        cache[i] = cache[i - 1] + cache[i - 2]

    return cache[n] % 10007


if __name__ == "__main__":
    assert solution(2) == 2, solution(2)
    assert solution(9) == 55, solution(9)
