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
    parsed = inputs.strip().split('\n')
    return parsed



def solve_example():
    inputs = load_inputs(test_input)
    return inputs

def solve_part1():
    inputs = load_inputs()
    return None

def solve_part2():
    inputs = load_inputs()
    return None


def run():

    start_time = time.time()
    print("Example:")
    print(solve_example())
    print("Runtime: {} seconds".format(time.time() - start_time))

    start_time = time.time()
    print("Part 1:")
    print(solve_part1())
    print("Runtime: {} seconds".format(time.time() - start_time))

    start_time = time.time()
    print("Part 2:")
    print(solve_part2())
    print("Runtime: {} seconds".format(time.time() - start_time))

run()
