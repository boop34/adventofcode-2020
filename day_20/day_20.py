#!/usr/bin/env python3

import itertools

# initialize a images dictionary to store the ids as keys and arrangements as
# values
imgs = {}

# fetch the input
with open('input.txt', 'r') as f:
    # get the id number and arrangement of tiles
    tiles = f.read().split('\n\n')
    # individual tiles have ids in the first line and the arrangement in the
    # other lines
    # iterate over the individual tiles
    for tile in tiles:
        # get the lines from the tiles block
        lines = tile.split('\n')
        # first line has the id
        id_ = int(lines[0].split()[1][:-1])
        # add the image in the imgs dictionary to the image id
        # 11 -> take the 10 lines ignore whitespaces at the end
        imgs[id_] = lines[1: 11]


# function to get the borders of the images
def get_borders(img):
    '''
    this function takes an img array and returs a list of four borders of the
    image and thier fliped versions as well

    1234
    5678    ->    [1234, 48dh, efgh, 15ae]
    abcd    ->    [4321, hd84, hgfe, ea51]
    efgh

    it returns a list of borders of the image
    '''
    # for the top border (original and fliped)
    tb, _tb = img[0], img[0][::-1]
    # for the bottom border (original and fliped)
    bb, _bb = img[-1], img[-1][::-1]
    # for the right border (original and fliped)
    rb = ''.join(s[-1] for s in img)
    _rb = rb[::-1]
    # for the left border (original and fliped)
    lb = ''.join(s[0] for s in img)
    _lb = lb[::-1]

    # return the list of borders
    return [tb, _tb, bb, _bb, rb, _rb, lb, _lb]


# function to get the number of shared borders
def intersection(b1, b2):
    '''
    this function takes two lists of boarders and check how many of them are
    intersecting

    it returns a number stating the number of shared border
    '''
    # get the count of the same borders between two list
    c = len(list(filter(lambda x: x[0] == x[1], itertools.product(b1, b2))))
    # return the count divided by 2 as 1 border is shared between two lists
    return c // 2


# get all the borders of all the images
borders = {i: get_borders(imgs[i]) for i in imgs}

# initialize a dictionary to keep count of the shared borders of each tile id
shared_borders = {}

# iterate over the tile ids
for t_id in borders:
    # initialize the shared border of the current tile id to be 0
    shared_borders[t_id] = 0
    # iterate over the tile ids for the current tile id
    for o_id in borders:
        # check if the other id and tile id are same
        if t_id == o_id:
            # skip
            continue
        # otherwise get the shared border count of them
        shared_borders[t_id] += intersection(borders[t_id], borders[o_id])

# now the corner most tile ids will have atmost 2 shared borders
# initialize a product variable
p = 1

# iterate over the borders
for tile_id in shared_borders:
    # check if the shared border count is 2
    if shared_borders[tile_id] == 2:
        # multiply the tile id
        p *= tile_id

# for the first puzzle
print(p)









# ************************ IGNORE ************************

# function to flip the image horizontally
def hor_flip(img_arr):
    '''
    this function takes an array of image lines that flips them horizontally

    1234          efgh
    5678    ->    abcd
    abcd          5678
    efgh          1234

    it returns an array with horizontally flipped image
    '''
    # get the length(height) of the image
    n = len(img_arr)
    # vertical flip
    ret_arr = img_arr[n:][::-1] + img_arr[:n][::-1]
    # return the flipped image
    return ret_arr


# function to flip the image vertically
def vert_flip(img_arr):
    '''
    this function takes an array of image lines that flips them vertically

    1234          4321
    5678    ->    8765
    abcd          dcba
    efgh          hgfe

    it returns an array with vertically flipped image
    '''
    # return the flipped image
    return [s[::-1] for s in img_arr]


# function to rotate the image by 90°
def rot_90(img_arr):
    '''
    this function takes an array of image lines that rotates 90° to the right

    1234          ea51
    5678    ->    fb62
    abcd          gc73
    efgh          hd84

    it returns an array with 90° rotated image
    '''
    # return the rotated array
    return [''.join(s[::-1]) for s in zip(*img_arr)]

def display(arr):
    for i in arr:
        print(i)
