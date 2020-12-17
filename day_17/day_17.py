#!/usr/bin/env python3

import itertools

# initialize a set to store the co-ordinates of the active cells in 3D
active1 = set()

# initialize a set to store the co-ordinates of the active cells in 4D
active2 = set()

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
                active1.add((r, c, 0))
                # for 4D it is in z=0, w=0 plane
                active2.add((r, c, 0, 0))

def active_cell(active, dimention):
    '''
    this function takes a active set containing tuples of the co-ordinates of
    active cells in either 3D or 4D and the corresponding dimention

    it returns the number of active cell after 6 cycles after appling some
    rules
    '''
    # iterate over for each 6 cycles
    for _ in range(6):
        # initialize a new set to store the active cells after the
        # current cycle
        new_active = set()
        # initialize a dictionary to keep track of the neighbouring
        # cells that has
        # active neighbours
        # key -> cell | value -> count of active neighbours
        active_neighbour = {}

        # now iterate over every active cell(x, y, z) of the curent state
        for cell in active:
            # get all the possible neighbouring co-ordinates
            # repeat = 3 -> 3 dimentions
            nco = list(itertools.product([-1, 0, 1], repeat=dimention))
            # iterate over the neighbouring co-ordinates
            for d in nco:
                # check if current cell
                if d == (0,) * dimention:
                    # skip
                    continue
                # for dimention == 3
                if len(d) == 3:
                    # unpack the cell co-ordinates
                    x, y, z = cell
                    # unpack the neighbour co-cordinates
                    dx, dy, dz = d
                    # construct the neighbour cell
                    n_cell = (x + dx, y + dy, z + dz)
                # for dimention == 4
                elif len(d) == 4:
                    # unpack the cell co-ordinates
                    x, y, z, w = cell
                    # unpack the neighbour co-cordinates
                    dx, dy, dz, dw = d
                    # construct the neighbour cell
                    n_cell = (x + dx, y + dy, z + dz, w + dw)
                # otherwise faulty input
                else:
                    return False

                # update the active neighbour dictionary
                active_neighbour[n_cell] = active_neighbour.get(n_cell, 0) + 1

        # now iterate through the active neighbour dictionary
        # cell -> cell co-ordinates | acn -> count of active neighbours
        for cell, acn in active_neighbour.items():
            # if a cell is active and exactly 2 or 3 of it's neighbors
            # are also active, the cell remains active else the cell
            # becomes inactive
            if cell in active and (acn == 2 or acn == 3):
                # add the current cell as an active cell
                new_active.add(cell)
            # if a cell is inactive but exactly 3 of its neighbors are active,
            # the cell becomes active else the cell remains inactive
            if cell not in active and acn == 3:
                # add the current cell as an active cell
                new_active.add(cell)

        # set the new active set as the initial active set
        active = new_active

    # return the length of the active set i.e total numbet of active cells
    return len(active)

# for the first puzzle
print(active_cell(active1, 3))

# for the second puzzle
print(active_cell(active2, 4))
