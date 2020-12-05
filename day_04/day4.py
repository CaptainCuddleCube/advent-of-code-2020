from re import match, split as re_split

codes = {
    "byr": lambda x: int(x) in range(1920, 2003),
    "iyr": lambda x: int(x) in range(2010, 2021),
    "eyr": lambda x: int(x) in range(2020, 2031),
    "hgt": lambda x: match(
        r"^(1(5[0-9]|6[0-9]|7[0-9]|8[0-9]|9[0-3])cm|(59|6[0-9]|7[0-6])in)$", x
    ),
    "hcl": lambda x: match(r"^#[a-f0-9]{6}$", x),
    "ecl": lambda x: x in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth"),
    "pid": lambda x: match(r"^[0-9]{9}$", x),
    # "cid": lambda x: True
}


def check_document(document, validation_checks):
    for code, rule in codes.items():
        if code not in document or not rule(document[code]) and validation_checks:
            return False
    return True


def parse_passports(raw_data: list, validation_checks=False):
    passports = []
    document = {}
    for row in raw_data:
        if row == "":
            document["valid"] = check_document(document, validation_checks)
            passports.append(document)
            document = {}
        else:
            code, value = row.split(":")
            document[code] = value
    return passports


valid_count = lambda passports: sum(pp["valid"] for pp in passports)
parser = lambda x: re_split(r"\n|\s", x)

if __name__ == "__main__":
    with open("data.txt", "r") as file:
        data = parser(file.read())
    print("Part one:", valid_count(parse_passports(data)))
    print("Part two:", valid_count(parse_passports(data, True)))
