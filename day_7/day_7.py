#!/usr/bin/env python3

from collections import defaultdict
import re

# regexp pattern to find the color codes
# lines are given in the format: <adjective> <color> <bag(s)>
# <adjective> <color> <bag(s)> contain <number> <adj> <color> <bag(s)> ...
pattern = r'(\w+\s\w+)\sbags?'

# initialize the dictionary to store the parent of a color code
# i.e key is the bag inside, value is the bag that contains the key
bags = defaultdict(list)

# fetch the input
with open('input.txt', 'r') as f:
    # process it line by line
    for line in f.readlines():
        # find all the color codes in the current line
        cc = re.findall(pattern, line.strip())
        # cc has the parent bag in the first index and child bags comes later
        for c in cc[1:]:
            bags[c].append(cc[0])

# recursive function to traverse through the bags dictionary and find all
# the bags containing a certain bag
def _rec_find(bags, c, s):
    '''
    this function takes the bags dictionary, a color code(c) and the set(s) to
    store the unique bags
    '''
    # base case: if the is not conatained by any other bag then just return
    if not bags[c]:
        return
    # iteratively go down each color coded bag that contains current bag
    for i in bags[c]:
        # add the current bag to the set
        s.add(i)
        # recursive call
        _rec_find(bags, i, s)

# wrapper function of the recursive _rec_find() function
def count_shiny():
    # initialize the set to keep track of the unique bags that can hold the
    # shiny gold bag
    s = set()
    # call the recursive function to prepare the set
    _rec_find(bags, 'shiny gold', s)
    # return the count of bags that can hold a shiny gold bag
    return len(s)

print(count_shiny())

