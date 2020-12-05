def parse_boarding_pass(b_pass):
    row = b_pass[0:7].replace("F", "0").replace("B", "1")
    seat = b_pass[7:10].replace("R", "1").replace("L", "0")
    return int(row, 2) * 8 + int(seat, 2)


def find_seat(ids):
    ids.sort()
    for i, v in enumerate(ids):
        if i > 0 and (v - ids[i - 1]) == 2:
            return v - 1


all_ids = lambda b_passes: [parse_boarding_pass(i) for i in b_passes]

if __name__ == "__main__":
    with open("data.txt", "r") as file:
        data = file.read().split("\n")

    print("Part 1:", max(all_ids(data)))
    print("Part 2:", find_seat(all_ids(data)))
