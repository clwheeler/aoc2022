import collections
import re
import sys
import time
from itertools import cycle

test_input = """x"""


def load_inputs(input_str=None):
    inputs = []

    if input_str:
        inputs = input_str
    else:
        with open('./inputs.txt', 'r') as f:
            inputs = f.read()

    parsed_test_input = parse_inputs(inputs)
    return parsed_test_input


def parse_inputs(inputs):
    grouped = inputs.strip().split('\n\n')
    grouped = [x.split("\n") for x in grouped]
    grouped = [[int(y) for y in x] for x in grouped]
    return grouped

def solve_part1(start):
    inputs = load_inputs()
    sums = [sum(x) for x in inputs]
    return max(sums)


def solve_part2(start):
    inputs = load_inputs()
    sums = [sum(x) for x in inputs]
    return sum(sorted(sums)[-3:])


def run():

    start_time = time.time()
    print("Part 1:")
    print(solve_part1(0))
    print("Runtime: {} seconds".format(time.time() - start_time))

    start_time = time.time()
    print("Part 2:")
    print(solve_part2(0))
    print("Runtime: {} seconds".format(time.time() - start_time))

run()
