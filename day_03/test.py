from day3 import counter

test_input = [
    "..##.......",
    "#...#...#..",
    ".#....#..#.",
    "..#.#...#.#",
    ".#...##..#.",
    "..#.##.....",
    ".#.#.#....#",
    ".#........#",
    "#.##...#...",
    "#...##....#",
    ".#..#...#.#",
]


assert counter(test_input, 3, 1) == 7, counter(test_input, 3, 1)
assert counter(test_input, 1, 1) == 2, counter(test_input, 1, 1)
assert counter(test_input, 5, 1) == 3, counter(test_input, 5, 1)
assert counter(test_input, 7, 1) == 4, counter(test_input, 7, 1)
assert counter(test_input, 1, 2) == 2, counter(test_input, 1, 2)
