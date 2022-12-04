import collections
import re
import sys
import time
from itertools import cycle

test_input_1 = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8"""
test_input_2 = test_input_1

def load_inputs(input_str=None):
    inputs = []

    if input_str:
        inputs = input_str
    else:
        with open('./inputs.txt', 'r') as f:
            inputs = f.read()

    parsed_test_input = parse_inputs(inputs)
    return parsed_test_input

Assignment = collections.namedtuple('Assignment', 'start end')

def parse_inputs(inputs):
    parsed = inputs.strip().split('\n')
    output = []
    for row in parsed:
        new_row = [elf.split('-') for elf in row.split(',')]
        new_row = [Assignment(int(y[0]), int(y[1])) for y in new_row]
        output.append(new_row)
    return output

"""
I assume part 2 will be to find all matches across all elves.
Should we invert the search logic to avoid n^2 comparisons:
- on first pass, look at every assignment and build a per-zone lookup. For 2-4, enter an row id in
2, 3, and 4
- elf_row_A/B
- after that, iterate through that zone lookup
- as you go, keep track of all the others that are fully contained.
"""
def solve_part1(input_str=None):
    inputs = load_inputs(input_str)
    included = []
    for row in inputs:
        if row[0].start >= row[1].start and row[1].end >= row[0].end:
            included.append(row)
        elif row[1].start >= row[0].start and row[0].end >= row[1].end:
            included.append(row)
    return len(included)

def solve_part2(input_str=None):
    inputs = load_inputs(input_str)
    included = []
    for row in inputs:
        if row[0].start >= row[1].start or row[1].end >= row[0].end:
            included.append(row)
        elif row[1].start >= row[0].start or row[0].end >= row[1].end:
            included.append(row)
    return len(included)


def run():

    start_time = time.time()
    print("Part 1:")
    print(solve_part1())
    print("Runtime: {} seconds".format(time.time() - start_time))

    start_time = time.time()
    print("Part 2:")
    print(solve_part2(test_input_2))
    print("Runtime: {} seconds".format(time.time() - start_time))

run()
