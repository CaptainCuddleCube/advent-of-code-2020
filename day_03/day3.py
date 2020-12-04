def counter(data, x_step, y_step):
    x, y, trees = 0, 0, 0
    while y < len(data):
        trees = trees + int(data[y][x] == "#")
        x, y = ((x + x_step) % len(data[0]), y + y_step)
    return trees


if __name__ == "__main__":
    with open("data.txt", "r") as file:
        in_dat = [i.strip("\n") for i in file.readlines()]

    print("Part 1:", counter(in_dat, 3, 1))
    print(
        "Part 2:",
        counter(in_dat, 3, 1)
        * counter(in_dat, 1, 1)
        * counter(in_dat, 5, 1)
        * counter(in_dat, 7, 1)
        * counter(in_dat, 1, 2),
    )
