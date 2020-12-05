from day5 import parse_boarding_pass, all_ids

tests = ["BFFFBBFRRR", "FFFBBBFRRR", "BBFFBBFRLL"]
assert all_ids(tests) == [567, 119, 820]
