def tokenize(raw):
    rules = {}
    for line in raw:
        colour, bags = line.split(" bags contain ")
        if bags == "no other bags.":
            rules[colour] = None
            continue
        rules[colour] = parse_inner_bags(bags.split(", "))
    return rules


def parse_inner_bags(data):
    inner_colours = {}
    for inner in data:
        count, adj, colour, _ = inner.split(" ")
        inner_colours[f"{adj} {colour}"] = int(count)
    return inner_colours


def can_hold(rules, value):
    if value is None:
        return False
    if "shiny gold" in value:
        return True
    for i in value:
        if can_hold(rules, rules[i]):
            return True
    return False


def counter(rules, name):
    if rules[name] is None:
        return 1
    count = 0
    for n, val in rules[name].items():
        inner = counter(rules, n)
        count += val * inner

    return count + 1


if __name__ == "__main__":
    with open("data.txt", "r") as file:
        data = file.read().strip().split("\n")
    rules = tokenize(data)
    print(
        "Part 1:",
        sum([1 for values in rules.values() if can_hold(rules, values)]),
    )
    print("Part 2:", counter(rules, "shiny gold") - 1)
