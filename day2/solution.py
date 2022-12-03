import collections
import functools
import re
import sys
import time
from itertools import cycle

test_input = """A Y
B X
C Z"""

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


def rps_scorer(input_str):
    ties = ['A X', 'B Y', 'C Z']
    wins = ['A Y', 'B Z', 'C X']
    round_score = 0
    scores = {'X': 1, 'Y':2, 'Z': 3}
    round_score += scores[input_str.split(' ')[1]]

    if input_str in ties:
        round_score += 3
    elif input_str in wins:
        round_score += 6

    return round_score

def rps_scorer_2(input_str):
    rocks = ['A Y', 'B X', 'C Z']
    papers = ['A Z', 'B Y', 'C X']
    round_score = 0
    scores = {'X': 0, 'Y':3, 'Z': 6}
    round_score += scores[input_str.split(' ')[1]]

    if input_str in rocks:
        round_score += 1
    elif input_str in papers:
        round_score += 2
    else:
        round_score += 3

    return round_score

def solve_example():
    inputs = load_inputs(test_input)
    result_list = [rps_scorer(x) for x in inputs]
    return inputs

def solve_part1():
    inputs = load_inputs()
    result_list = [rps_scorer(x) for x in inputs]
    return sum(result_list)

def solve_part2():
    inputs = load_inputs()
    result_list = [rps_scorer_2(x) for x in inputs]
    return sum(result_list)


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
