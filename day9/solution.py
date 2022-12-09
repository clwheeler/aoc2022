import collections
import re
import sys
import time
from itertools import cycle

test_input_1 = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2"""


test_input_2 = """R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20"""

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

def get_dir(dirstring):
    if dirstring == 'L':
        return (-1, 0)
    if dirstring == 'R':
        return (1, 0)
    if dirstring == 'D':
        return (0, -1)
    if dirstring == 'U':
        return (0, 1)

def move_h(hpos, dirstring):
    delta = get_dir(dirstring)
    return (hpos[0] + delta[0], hpos[1] + delta[1])

def manhattan_distance(a, b):
    dist = sum([abs(a[0] - b[0]), abs(a[1] - b[1])])
    return dist

# use average, but it will always a difference of 2
def follow(hpos, tpos):
    # overlap
    x_diff = hpos[0] - tpos[0]
    y_diff = hpos[1] - tpos[1]

    if hpos == tpos:
        pass
    # same x
    elif x_diff == 0:
        if manhattan_distance(hpos, tpos) > 1:
            deltax = 0
            deltay = (y_diff) / abs(y_diff)
            return (tpos[0] + deltax, tpos[1] + deltay)
    # same y
    elif y_diff == 0:
        if manhattan_distance(hpos, tpos) > 1:
            deltax = (x_diff) / abs(x_diff)
            deltay = 0
            return (tpos[0] + deltax, tpos[1] + deltay)
    else:
        if manhattan_distance(hpos, tpos) > 2:
            deltax = (x_diff) / abs(x_diff)
            deltay = (y_diff) / abs(y_diff)
            return (tpos[0] + deltax, tpos[1] + deltay)
        # move diag

    return tpos

def solve_part1(input_str=None):
    inputs = load_inputs(input_str)
    segments = [(0, 0), (0, 0)]

    all_t_locations = [segments[-1]]

    for instruction in inputs:
        direction = instruction.split(' ')[0]
        distance = int(instruction.split(' ')[1])
        print(direction, distance)
        for x in range(distance):
            for idx in range(len(segments)):
                if idx == 0:
                    segments[0] = move_h(segments[0], direction)
                else:
                    this = segments[idx]
                    prev = segments[idx-1]
                    segments[idx] = follow(prev, this)

            all_t_locations.append(segments[-1])

            # print(f"H: {segments[0]}  T: {segments[-1]}")

    print(all_t_locations)
    return(len(list(set(all_t_locations))))

def solve_part2(input_str=None):
    inputs = load_inputs(input_str)
    segments = [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)]

    all_t_locations = [segments[-1]]

    for instruction in inputs:
        direction = instruction.split(' ')[0]
        distance = int(instruction.split(' ')[1])
        print(direction, distance)
        for x in range(distance):
            for idx in range(len(segments)):
                if idx == 0:
                    segments[0] = move_h(segments[0], direction)
                else:
                    this = segments[idx]
                    prev = segments[idx-1]
                    segments[idx] = follow(prev, this)

            all_t_locations.append(segments[-1])

            # print(f"H: {segments[0]}  T: {segments[-1]}")

    print(all_t_locations)
    return(len(list(set(all_t_locations))))


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
