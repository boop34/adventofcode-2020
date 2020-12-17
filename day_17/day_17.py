#!/usr/bin/env python3

import itertools

# initialize a set to store the co-ordinates of the active cells
active = set()

# fetch the input
with open('input.txt', 'r') as f:
    # parse it line by line
    for r, line in enumerate(f.readlines()):
        # parse the current line
        for c, cell in enumerate(line.strip()):
            # check if the cell is active
            if cell == '#':
                # add the co-ordinate to the active set
                # in the begining the cells are the at the z=0 plane
                active.add((r, c, 0))

# iterate over for each 6 cycles
for _ in range(6):
    # initialize a new set to store the active cells after the current cycle
    new_active = set()
    # initialize a dictionary to keep track of the neighbouring cells that has
    # active neighbours
    # key -> cell | value -> count of active neighbours
    active_neighbour = {}

    # now iterate over every active cell(x, y, z) of the curent state
    for x, y, z in active:
        # get all the possible neighbouring co-ordinates
        # repeat = 3 -> 3 dimentions
        nco = list(itertools.product([-1, 0, 1], repeat=3))
        # iterate over the neighbouring co-ordinates
        for dx, dy, dz in nco:
            # check if current cell
            if (dx, dy, dz) == (0, 0, 0):
                # skip
                continue
            # construct the neighbour cell
            n_cell = (x + dx, y + dy, z + dz)
            # update the active neighbour dictionary
            active_neighbour[n_cell] = active_neighbour.get(n_cell, 0) + 1

    # now iterate through the active neighbour dictionary
    # cell -> cell co-ordinates | acn -> count of active neighbours
    for cell, acn in active_neighbour.items():
        # if a cell is active and exactly 2 or 3 of it's neighbors are also
        # active, the cell remains active else the cube becomes inactive
        if cell in active and (acn == 2 or acn == 3):
            # add the current cell as an active cell
            new_active.add(cell)
        # if a cell is inactive but exactly 3 of its neighbors are active,
        # the cube becomes active else the cell remains inactive
        if cell not in active and acn == 3:
            # add the current cell as an active cell
            new_active.add(cell)

    # set the new active set as the initial active set
    active = new_active

# for the first puzzle
print(len(active))
