import collections
import itertools
import re
import sys
import time

test_input_1 = """zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"""
test_input_2 = """mjqjpqmgbljsphdztnvjfqwrcgsmlb"""

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

def sliding_window(iterable, n):
    # sliding_window('ABCDEFG', 4) --> ABCD BCDE CDEF DEFG
    it = iter(iterable)
    window = collections.deque(itertools.islice(it, n), maxlen=n)
    if len(window) == n:
        yield tuple(window)
    for x in it:
        window.append(x)
        yield tuple(window)

def solve_part1(input_str=None):
    inputs = load_inputs(input_str)
    input_str = inputs[0]
    for idx, group in enumerate(sliding_window(input_str, 4)):
        c = collections.Counter(group)
        if len(c.keys()) == 4:
            return idx+4

def solve_part2(input_str=None):
    inputs = load_inputs(input_str)
    input_str = inputs[0]
    for idx, group in enumerate(sliding_window(input_str, 14)):
        c = collections.Counter(group)
        if len(c.keys()) == 14:
            return idx+14


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
