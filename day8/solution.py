import collections
import re
import sys
import time
from itertools import cycle

test_input_1 = """30373
25512
65332
33549
35390"""
test_input_2 = test_input_1

Tree = collections.namedtuple('Tree', 'x y')

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
    # access with grid[x][y]
    int_grid = [[int(col) for col in row] for row in parsed]

    return int_grid

def cast_rays_x(input_grid, HEIGHT, WIDTH, reverse):
    visible_trees = []

    for x in range(HEIGHT):
        previous_height = -1
        for relative_y in range(WIDTH):
            if reverse:
                absolute_y = (WIDTH-1) - relative_y
            else:
                absolute_y = relative_y
            this_height = input_grid[x][absolute_y]
            if this_height > previous_height:
                previous_height = this_height
                visible_trees.append(Tree(x, absolute_y))

    return visible_trees

def cast_rays_y(input_grid, HEIGHT, WIDTH, reverse):
    visible_trees = []

    for y in range(WIDTH):
        previous_height = -1
        for relative_x in range(HEIGHT):
            if reverse:
                absolute_x = (HEIGHT-1) - relative_x
            else:
                absolute_x = relative_x
            this_height = input_grid[absolute_x][y]
            if this_height > previous_height:
                previous_height = this_height
                visible_trees.append(Tree(absolute_x, y))

    return visible_trees

"""
Cast rays from the edges until val(x+1) <= val(x)
"""
def solve_part1(input_str=None):
    input_grid = load_inputs(input_str)
    HEIGHT = len(input_grid)
    WIDTH = len(input_grid[0])

    # lets keep track of location of all trees, so we can dedupe
    # list of tree tuples
    visible_trees = []

    # TODO: do height 0 trees count as visible?
    visible_trees += cast_rays_x(input_grid, HEIGHT, WIDTH, False)
    visible_trees += cast_rays_x(input_grid, HEIGHT, WIDTH, True)
    visible_trees += cast_rays_y(input_grid, HEIGHT, WIDTH, False)
    visible_trees += cast_rays_y(input_grid, HEIGHT, WIDTH, True)

    visible_trees = list(set(visible_trees))

    return len(visible_trees)


def cast_from_tree(input_grid, start, delta_x, delta_y):
    HEIGHT = len(input_grid)
    WIDTH = len(input_grid[0])

    this_height = input_grid[start.x][start.y]

    this_x = start.x
    this_y = start.y
    visible_count = 0


    while(True):
        if this_x + delta_x < 0 or this_x + delta_x >= HEIGHT:
            print(f"        Edge detected, {visible_count}")
            return visible_count
        if this_y + delta_y < 0 or this_y + delta_y >= WIDTH:
            print(f"        Edge detected, {visible_count}")
            return visible_count
        this_x = this_x + delta_x
        this_y = this_y + delta_y

        next_height = input_grid[this_x][this_y]
        if next_height < this_height:
            visible_count += 1
        else:
            visible_count += 1
            print(f"        Tall Tree detected, {visible_count}")
            return visible_count

def solve_part2(input_str=None):

    input_grid = load_inputs(input_str)
    all_scores = []

    HEIGHT = len(input_grid)
    WIDTH = len(input_grid[0])

    for x in range(HEIGHT):
        for y in range(WIDTH):
            score = 1

            print(f"Checking {x}, {y}...")
            print("    Look Down")
            score *= cast_from_tree(input_grid, Tree(x, y), 0, 1)
            print("    Look Up")
            score *= cast_from_tree(input_grid, Tree(x, y), 0, -1)
            print("    Look Right")
            score *= cast_from_tree(input_grid, Tree(x, y), 1, 0)
            print("    Look Left")
            score *= cast_from_tree(input_grid, Tree(x, y), -1, 0)
            all_scores.append(score)

    print(all_scores)
    return max(all_scores)


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
