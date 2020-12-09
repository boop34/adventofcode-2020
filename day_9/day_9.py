#!/usr/bin/env python3

from input import arr

# function to check the validity of the number
def is_valid(n, l, h, arr):
    '''
    this function takes an number(n), a lower bound(l), a upper bound(h) and
    an array(arr), and checks if n can be made by adding any two numbers from
    the array in between the upper and lower bound

    returns True or Flase
    '''
    # initialize a dictionary to access the numbers in O(n)
    num_dict = {i: True for i in arr[l: h]}

    # iterate over the numbers of the array
    for i in arr:
        # check if (n-i) is present in the array and if (n-i) and i are not
        # same
        if num_dict.get(n - i, False) and (n - i) != i:
            return True

    # otherwise return false
    return False

# initialize the length of the preamble and length of the input
l, n = 25, len(arr)

# initialize the staring index which is the index after the preamble
i = l   # as 0 based index

# loop over till we reach the end of the input
while i < n:
    # check the validity of the number
    if not is_valid(arr[i], i - l, i, arr):
        # if not valid print the number
        print(arr[i])
        break
    # increase the index
    i += 1

