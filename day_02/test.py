from day2 import valid_count, is_valid_new_policy

test_data = [
    "1-3 a: abcde",
    "1-3 b: cdefg",
    "2-9 c: ccccccccc",
]

assert valid_count(test_data) == 2, valid_count(test_data)
assert valid_count(test_data, is_valid_new_policy) == 1, valid_count(
    test_data, is_valid_new_policy
)
