import collections
import random
import re
import string
import sys
import time
from itertools import cycle

test_input_1 = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""

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

FILE = "FILE"
DIR = "DIR"

class FSNode:

    def __init__(self, parent, kind, name="root", size=0):
        self.parent = parent
        self.kind = kind
        self.name = name
        self.size = size
        self.children = []

    def addChild(self, child):
        self.children.append(child)
        child.setParent(self)

    def getChild(self, name):
        for child in self.children:
            if child.name == name:
                return child
        return None

    def setParent(self, parent):
        self.parent = parent

    def getDirSizes(self, agg):
        if self.kind == FILE:
            return self.size
        else:
            sizes = [child.getDirSizes(agg) for child in self.children]
            dirSize = sum(sizes)
            # i don't want to bother with full paths, so just give each folder a unique id
            letters = string.ascii_lowercase
            dir_id = ''.join(random.choice(letters) for i in range(20))
            agg[dir_id] = dirSize
            return dirSize

    def getSize(self):
        if self.kind == FILE:
            return self.size
        else:
            sizes = [child.getSize() for child in self.children]
            return sum(sizes)

    def __str__(self):
        pname = 'NONE'
        if self.parent:
            pname = self.parent.name
        if self.kind == DIR:
            return f"[ Type: {self.kind} | Name: {self.name} ]"
        if self.kind == FILE:
            return f"[ Type: {self.kind} | Name: {self.name} | Size: {self.size}]"

    def PrintTree(self, indent = 0):
        indent_str = "    " * indent
        print(f"{indent_str}{self}")
        for child in self.children:
            child.PrintTree(indent + 1)


def constructTree(inputs):
    root = FSNode(None, DIR)

    # this should be a pointer?
    current_node = root

    for cmd in inputs:
        if re.match(r'\$ cd (.*)', cmd):
            dir_name = re.match(r'\$ cd (.*)', cmd).groups()[0]
            if dir_name == '/':
                current_node = root
            elif dir_name == '..':
                current_node = current_node.parent
            else:
                findChild = current_node.getChild(dir_name)
                if findChild:
                    current_node = findChild
                else:
                    created = FSNode(current_node, DIR, dir_name)
                    current_node.addChild(created)
                    current_node = created
        elif cmd == '$ ls':
            pass
        else:
            if re.match(r'(\d+) (.*)', cmd):
                size = re.match(r'(\d+) (.*)', cmd).groups()[0]
                filename = re.match(r'(\d+) (.*)', cmd).groups()[1]
                created = FSNode(current_node, FILE, filename, int(size))
                current_node.addChild(created)

    return root


def solve_part1(input_str=None):
    inputs = load_inputs(input_str)

    root = constructTree(inputs)

    # root.PrintTree()
    dirSizeDict = {}
    root.getDirSizes(dirSizeDict)
    targetSizes = [dirSizeDict[x] for x in dirSizeDict.keys() if dirSizeDict[x] <= 100000]
    return sum(targetSizes)

def solve_part2(input_str=None):
    inputs = load_inputs(input_str)

    root = constructTree(inputs)

    # root.PrintTree()
    dirSizeDict = {}
    root_size = root.getSize()
    freespace = 70000000 - root_size
    required_space = 30000000 - freespace

    # find dir with size > required_space and closest to required_space
    root.getDirSizes(dirSizeDict)
    targetSizes = [dirSizeDict[x] for x in dirSizeDict.keys() if dirSizeDict[x] >= required_space]
    return min(targetSizes)


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
