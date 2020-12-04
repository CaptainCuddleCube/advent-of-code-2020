def parse(data):
    counts, char, password = data.split(" ")
    return (char[0], password, *(int(i) for i in counts.split("-")))


def is_valid_old_policy(char, password, mini, maxi):
    return password.count(char) in range(mini, maxi + 1)


def is_valid_new_policy(char, password, mini, maxi):
    return (password[mini - 1], password[maxi - 1]).count(char) == 1


def valid_count(data, policy=is_valid_old_policy):
    return len([i for i in data if policy(*parse(i))])


if __name__ == "__main__":
    with open("data.txt", "r") as file:
        passwords = [i.strip("\n") for i in file.readlines()]
    print("Part 1:", valid_count(passwords))
    print("Part 2:", valid_count(passwords, is_valid_new_policy))
