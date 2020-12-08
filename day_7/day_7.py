#!/usr/bin/env python3

from collections import defaultdict
import re

# regexp pattern to find the color codes
# lines are given in the format: <adjective> <color> <bag(s)>
# <adjective> <color> <bag(s)> contain <number> <adj> <color> <bag(s)> ...
pattern = r'(\w+\s\w+)\sbags?'

# initialize the dictionary to store the parent of a color code
# i.e key is the bag inside, value is the bag that contains the key
parent_bags = defaultdict(list) # key -> child, value -> parent

# initialize the dictionary to store the children of a color code
# i.e key is the bag outside, value is a tuple of the bag that is contained in
# the key and the count of those child bags
child_bags = defaultdict(list) # key -> parent, value -> (child, count)

# fetch the input
with open('input.txt', 'r') as f:
    # process it line by line
    for line in f.readlines():
        # find all the color codes in the current line
        cc = re.findall(pattern, line.strip())
        # find the number of child bags
        n = re.findall(r'\d+', line.strip())
        # convert the numbers into integers
        n = list(map(int, n))
        # there are no other bags inside
        if not n:
            # fill the child bag with value of parent bag
            parent_bags['no other'].append(cc[0].strip())
            # fill the parent bag with value of child bag
            child_bags[cc[0].strip()] = 0
        # if there are child bags present
        else:
            # cc has the parent bag in the first index and child bags comes
            # later
            for c in zip(cc[1:], n):
                # fill the child bag with the value of parent bag
                parent_bags[c[0].strip()].append(cc[0].strip())
                # fill the parent bag with the value of child bag
                child_bags[cc[0].strip()].append(c)

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
    for bag in bags[c]:
        # add the current bag to the set
        s.add(bag)
        # recursive call
        _rec_find(bags, bag, s)

# recursive function to find the number of bags present in a single bag
def _rec_count(bags, c):
    # base case: current bag contains no other bags
    if not bags[c]:
        return 1
    tmp = 0
    # now iterate for each child bag of current bag
    for bag in bags[c]:
        # unpack the tuple of (bag color, count)
        bc, n = bag
        # recursive call
        tmp += n * _rec_count(bags, bc)

    # adding 1 as we have to consider the current bag
    return tmp + 1

# wrapper function of the recursive _rec_find() function
def count_shiny():
    # initialize the set to keep track of the unique bags that can hold the
    # shiny gold bag
    s = set()

    # call the recursive function to prepare the set for 'how many bags can
    # hold the shiny gold bag'
    _rec_find(parent_bags, 'shiny gold', s)

    # return the count of bags that can hold a shiny gold bag and the set of
    # bags that shiny gold bag contains
    return len(s)

# initialize a dictionary to calculate the value of every color coded bag
# NOTE: we are considering the bag itself included in the value so when
# determining the value of a bag we have subtract 1 from it's value
value_dict = defaultdict(int)

# populate the value_dict
for i in child_bags:
    value_dict[i] = _rec_count(child_bags, i)

# get the length of the bags that contain the shiny gold bag and the set of
# bags that shiny bag can hold
l = count_shiny()

# initialize the counter
c = 0
# get the total count of bags that shiny gold contains
for i in child_bags['shiny gold']:
    c += value_dict[i[0]] * i[1]

# first puzzle
print(l)
# second puzzle
print(c)

