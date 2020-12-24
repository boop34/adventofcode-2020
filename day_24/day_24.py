#!/usr/bin/env python3

from collections import defaultdict
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
visited = defaultdict(int)

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
    visited[origin] += 1

# for the first puzzle
print(sum([1 for i in visited if visited[i] == 1]))

# initialize the black tiles set
black_tiles = set()

# add the present black tiles
for i in visited:
    # check if the tile is black
    if visited[i] == 1:
        # add the tile to the set
        black_tiles.add(i)

# loop for 100 times
for _ in range(100):
    # initialize a dictionary to keep track of the neighbours of a black tile
    neighbours = defaultdict(int)

    # iterate over the black tiles
    for x, y in black_tiles:
        # check if y is even or odd
        if y % 2 == 0:
            delta = [deltas_even[i] for i in deltas_even]
        else:
            delta = [deltas_odd[i] for i in deltas_odd]

        # apply the deltas
        for dx, dy in delta:
            neighbours[(x + dx, y + dy)] += 1

    # initialize a new black tiles set
    new_black_tiles = set()

    # iterate over the neighbours dictionary
    for neighbour in neighbours:
        # check if the current neighbour is a black tile
        if neighbour in black_tiles:
            # check if 0 or more than 2 black tile immediately adjacent to it
            if neighbours[neighbour] == 0 or neighbours[neighbour] > 2:
                # don't add te current tile to the new black tiles set
                pass
            # otherwise
            else:
                # add the current tile to the new black tiles set
                new_black_tiles.add(neighbour)
        # otherwise it's a white tile
        elif neighbours[neighbour] == 2:
            # add the tile to the new black tiles set
            new_black_tiles.add(neighbour)

    # set the initial black tiles to the new black tiles set
    black_tiles = new_black_tiles

# for the second puzzle
print(len(black_tiles))
