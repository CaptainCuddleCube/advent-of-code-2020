from functools import reduce

split_data = lambda raw: [i.split("\n") for i in raw.split("\n\n")]
reducer = lambda fn: lambda x, y: set(list(y)) if x is None else fn(x, set(list(y)))
applier = lambda x, set_fn: sum([len(reduce(reducer(set_fn), i, None)) for i in x])

if __name__ == "__main__":
    with open("data.txt", "r") as file:
        data = split_data(file.read().strip())
    print("Part 1:", applier(data, set.union))
    print("Part 2:", applier(data, set.intersection))
