from itertools import combinations
from functools import reduce


def find_sum(d, sum_depth=1):
    return next(
        reduce(lambda x, y: x * y, x, 1) * (2020 - sum(x))
        for x in combinations(d, sum_depth)
        if (2020 - sum(x)) in d
    )


if __name__ == "__main__":
    with open("data.txt", "r") as f:
        data = set(int(line.strip("\n")) for line in f.readlines())
    print("q1:", find_sum(data))
    print("q2:", find_sum(data, 2))
