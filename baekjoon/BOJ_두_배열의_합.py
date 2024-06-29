# BOJ 2143 두 배열의 합
from collections import defaultdict


def get_input():
    f = open("input_files/2143_input.txt", "r")
    t: int = int(f.readline())
    n: int = int(f.readline())
    an: list[int] = list(map(int, f.readline().split()))
    m: int = int(f.readline())
    bm: list[int] = list(map(int, f.readline().split()))

    return t, n, an, m, bm


def get_sums_dict(n: int, xn: list[int]) -> dict[int, int]:
    sums_dict = defaultdict(int)
    for i in range(n):
        for j in range(i, n):
            sums_dict[sum(xn[i : j + 1])] += 1
    return sums_dict


def get_solution(t: int, n: int, an: list[int], m: int, bm: list[int]) -> int:
    ans = 0
    an_dict = get_sums_dict(n, an)
    bn_dict = get_sums_dict(m, bm)

    for a_sum, a_count in an_dict.items():
        b_sum = t - a_sum
        ans += a_count * bn_dict.get(b_sum, 0)
    return ans


if __name__ == "__main__":
    t, n, an, m, bm = get_input()
    solution = get_solution(t, n, an, m, bm)
    assert solution == 7, f"Expected Result : 7, Returned Result : {solution}"
