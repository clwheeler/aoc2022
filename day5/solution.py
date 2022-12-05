import collections
import copy
import re
import sys
import time
from itertools import cycle

test_input_1 = """x"""
test_input_2 = test_input_1

INIT_STATE = [
    ["G", "F", "V", "H", "P", "S"],
    ["G", "J", "F", "B", "V", "D", "Z", "M"],
    ["G", "M", "L", "J", "N"],
    ["N", "G", "Z", "V", "D", "W", "P"],
    ["V", "R", "C", "B"],
    ["V", "R", "S", "M", "P", "W", "L", "Z"],
    ["T", "H", "P"],
    ["Q", "R", "S", "N", "C", "H", "Z", "V"],
    ["F", "L", "G", "P", "V", "Q", "J"],
]

def load_inputs(input_str=None):
    inputs = []

    if input_str:
        inputs = input_str
    else:
        with open('./inputs.txt', 'r') as f:
            inputs = f.read()

    parsed_test_input = parse_inputs(inputs)
    return parsed_test_input

# Tuple : quantity, source, dest
def parse_inputs(inputs):
    parsed = inputs.strip().split('\n')
    instructions = []
    for line in parsed:
        if "move" in line:
            vals = re.search(r"move (\d+) from (\d+) to (\d+)", line)
            instructions.append(tuple([x for x in map(lambda x: int(x), vals.groups())]))

    return instructions

def solve_part1(input_str=None):
    inputs = load_inputs(input_str)
    STATE = copy.deepcopy(INIT_STATE)

    for row in inputs:
        src = STATE[row[1] - 1]
        dest = STATE[row[2] - 1]
        for x in range(row[0]):
            elem = src.pop()
            dest.append(elem)

    output = []
    for col in STATE:
        output.append(col[-1])

    return "".join(output)

def solve_part2(input_str=None):
    inputs = load_inputs(input_str)
    STATE = copy.deepcopy(INIT_STATE)

    for row in inputs:
        src = STATE[row[1] - 1]
        dest = STATE[row[2] - 1]
        elems = []
        for x in range(row[0]):
            elems = [src.pop()] + elems
        dest += elems

    output = []
    for col in STATE:
        output.append(col[-1])

    return "".join(output)


def run():

    start_time = time.time()
    print("Part 1:")
    print(solve_part1())
    print("Runtime: {} seconds".format(time.time() - start_time))

    start_time = time.time()
    print("Part 2:")
    print(solve_part2())
    print("Runtime: {} seconds".format(time.time() - start_time))

run()
