#!/usr/bin/env python3

def count_trees(mat, h, n, r, d):
    '''
    given a matrix 'mat' of 'h' rows and 'n' columns print the number of trees    that will be encountered if starting from (0, 0) we go 'r' steps to the
    right and 'd' steps to the down in each step
    '''
    # initialize the starting co-ordinates
    x, y = 0, 0
    # initialize the tree counter
    tree_count = 0

    # untill we get to the bottom of the matrix
    while y < h - 1:
        # update the co-ordinates
        x = (x + r) % n
        y += d

        # check if there is a tree at the (x, y) position
        if mat[y][x] == '#':
            tree_count += 1

    # return the number of trees encountered
    return tree_count

# get the number of rows in the matrix
h = 0

# make a 2D matrix out of the input
mat = []

# get the inputs
with open('input.txt', 'r') as f:
    # read the inputs line by line
    for line in f.readlines():
        # make a single row out of the line
        tmp = [i.strip() for i in line.strip()]
        # append the row to the matrix
        mat.append(tmp)
        # increment the row count
        h += 1

# get the length of each row
n = len(mat[0])

# for slope: {right 1, down 1}
tc1 = count_trees(mat, h, n, 1, 1)

# for slope: {right 3, down 1}
tc2 = count_trees(mat, h, n, 3, 1)

# for slope: {right 5, down 1}
tc3 = count_trees(mat, h, n, 5, 1)

# for slope: {right 7, down 1}
tc4 = count_trees(mat, h, n, 7, 1)

# for slope: {right 1, down 2}
tc5 = count_trees(mat, h, n, 1, 2)

# for the first puzzle
print(tc2)
# for the second puzzle
print(tc1 * tc2 * tc3 * tc4 * tc5)

