#!/usr/bin/env python3

import re

# direction extraction pattern
pat = r'(e|se|sw|w|nw|ne)'

'''
  ,   ,   ,   ,   ,
 / \ / \ / \ / \ /
| A1| A2| A3| A4|
 \ / \ / \ / \ / \
  | B1| B2| B3| B4|
 / \ / \ / \ / \ /
| C1| C2| C3| C4|
 \ / \ / \ / \ / \
  '   '   '   '   '
'''
# initialize the dictionary of deltas for each direction
# respective of (x, y) where y is even
deltas_even = {'e': (1, 0),'se': (1, -1),'sw': (0, -1),'w': (-1, 0),
          'nw': (0, 1),'ne': (1, 1)}

# respective of (x, y) where y is odd
deltas_odd = {'e': (1, 0),'se': (0, -1),'sw': (-1, -1),'w': (-1, 0),
          'nw': (-1, 1),'ne': (0, 1)}

# initialize a directions list
dirs = []

# fetch the inputs
with open('input.txt', 'r') as f:
    # parse it line by line
    for line in f.readlines():
        # extract the directions from the current line and append them to the
        # global directions list
        dirs.append(re.findall(pat, line.strip()))

# initialize a visited dictionary to store the count of how many times have the
# tile been visited
visited = {}

# iterate over the list of directions
for step in dirs:
    # always start from the reference centre point
    origin = (0, 0)
    # iterate over individual direction on the current step
    for d in step:
        # check if the y is odd or even
        if origin[1] % 2 == 0:
            # get the delta value of the current direction
            delta = deltas_even[d]
        else:
            # get the delta value of the current direction
            delta = deltas_odd[d]
        # update the point
        origin = (origin[0] + delta[0], origin[1] + delta[1])
    # increment the visited count of the tile
    visited[origin] = visited.get(origin, 0) + 1

# for the first puzzle
print(sum([1 for i in visited if visited[i] == 1]))
