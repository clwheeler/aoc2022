import collections
import re
import sys
import time
from itertools import cycle

test_input_1 = """addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop"""

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

def compute_cycles(inputs):
    reg_value = 1
    cycle_history = ['']

    for command in inputs:
        c_type = re.match(r'(\w+)(.*)', command).groups()[0]
        val = re.match(r'(\w+)(.*)', command).groups()[1]
        if c_type == "noop":
            cycle_history.append(reg_value)
        else:
            cycle_history.append(reg_value)
            cycle_history.append(reg_value)
            reg_value = reg_value + int(val)

    return cycle_history

def solve_part1(input_str=None):
    inputs = load_inputs(input_str)

    cycle_history = compute_cycles(inputs)

    # Find the signal strength during the 20th, 60th, 100th, 140th, 180th, and 220th cycle
    interesting  = cycle_history[20:221:40]
    strengths = [(20+(i*40)) * v for i, v in enumerate(interesting)]
    return sum(strengths)


def solve_part2(input_str=None):
    inputs = load_inputs(input_str)
    cycle_history = compute_cycles(inputs)

    output = []
    # for pixel_index in range(240):

    for cycle_count, reg_val in enumerate(cycle_history):
        if cycle_count == 0:
            continue
        # On cycle = 1, draw pixel = 0
        pixel_index = (cycle_count - 1) % 40
        if abs(pixel_index - reg_val) < 2:
            output.append('#')
        else:
            output.append('.')

        if pixel_index > 0 and pixel_index % 39 == 0:
            output.append('\n')
        if pixel_index > 0 and pixel_index % 239 == 0:
            output.append('\n')

    output_str = ''.join(output)
    return output_str


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
