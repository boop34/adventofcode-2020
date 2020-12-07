#!/usr/bin/env python3

# initialize the (x, y) cor-ordinates
x, y = 0, 0

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

# initialize the tree count
tree_count = 0

# untill we get to the bottom of the matrix
while y < h - 1:
    # update the co-ordinates
    x = (x + 3) % n
    y += 1
    # check if there is a tree at the (x, y) position
    if mat[y][x] == '#':
        tree_count += 1

print(tree_count)
