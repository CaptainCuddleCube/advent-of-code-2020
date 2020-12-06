from day6 import split_data, applier

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

assert applier(split_data(test_data.strip()), set.union) == 11
assert applier(split_data(test_data.strip()), set.intersection) == 6
