from day6 import split_data, counter

test_data = """
abc

a
b
c

ab
ac

a
a
a
a

b
"""

parsed_test_data = split_data(test_data.strip().split("\n\n"))

assert counter(parsed_test_data, set.union) == 11
assert counter(parsed_test_data, set.intersection) == 6
