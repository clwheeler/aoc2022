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


# This could be done with some math and rounding to just get position based on
# higher resolution, but doing it explicitly is clearer
def follow(lead, follower):
    deltax = lead[0] - follower[0]
    deltay = lead[1] - follower[1]
    man_dist = manhattan_distance(lead, follower)

    if deltax != 0:
        deltax = (deltax) / abs(deltax)
    if deltay != 0:
        deltay = (deltay) / abs(deltay)

    # same x or y
    if deltax == 0 or deltay == 0:
        if man_dist > 1:
            return (follower[0] + deltax, follower[1] + deltay)
    # diag
    elif man_dist > 2:
        return (follower[0] + deltax, follower[1] + deltay)

    # no movement
    return follower

def solve_part1(input_str=None):
    inputs = load_inputs(input_str)
    segments = [(0, 0), (0, 0)]

    all_t_locations = [segments[-1]]

    for instruction in inputs:
        direction = instruction.split(' ')[0]
        distance = int(instruction.split(' ')[1])
        # print(direction, distance)
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

    return(len(list(set(all_t_locations))))

def solve_part2(input_str=None):
    inputs = load_inputs(input_str)
    segments = [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)]

    all_t_locations = [segments[-1]]

    for instruction in inputs:
        direction = instruction.split(' ')[0]
        distance = int(instruction.split(' ')[1])
        # print(direction, distance)
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

    # print(all_t_locations)
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
