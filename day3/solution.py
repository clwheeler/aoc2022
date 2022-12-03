import collections
import re
import sys
import time
from itertools import cycle

test_input_1 = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""

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

def parse_inputs(inputs):
    parsed = inputs.strip().split('\n')
    return parsed

PRIOS = ' abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

def solve_part1(input_str=None):
    inputs = load_inputs(input_str)
    all_shared = []
    for row in inputs:
        mid = int(len(row)/2)
        halves = [row[0:mid], row[mid:]]
        shared = [x for x in halves[0] if x in halves[1]][0]
        all_shared.append(shared)
    prio = [PRIOS.index(x) for x in all_shared]
    return sum(prio)


def solve_part2(input_str=None):
    inputs = load_inputs(input_str)
    all_shared = []
    input_iter = iter(inputs)

    for row in input_iter:
        elems = [row]
        elems.append(next(input_iter))
        elems.append(next(input_iter))
        shared = [x for x in elems[0] if x in elems[1] and x in elems[2]][0]
        all_shared.append(shared)
    prio = [PRIOS.index(x) for x in all_shared]
    return sum(prio)


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
