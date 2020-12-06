split_data = lambda x: [[set(list(j)) for j in i.split("\n")] for i in x]
counter = lambda data, set_fn: sum(len(set_fn(*s)) for s in data)


if __name__ == "__main__":
    with open("data.txt", "r") as file:
        data = split_data(file.read().strip().split("\n\n"))
    print("Part 1:", counter(data, set.union))
    print("Part 2:", counter(data, set.intersection))
