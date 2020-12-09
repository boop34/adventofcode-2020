#!/usr/bin/env python3

from input import arr
import sys

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
        # store the number
        invalid = arr[i]
        # if not valid print the number
        print(arr[i])
        break
    # increase the index
    i += 1

# iterate over every number in input
for i in range(n):
    # initialize the sum to be the current number
    s = 0
    # now try adding every other number to get the invalid number
    for j in range(i, n):
        # add the numbers
        s += arr[j]
        # check if the sum is equal to invalid number
        if s == invalid:
            # find the maximum and minimum in between (i, j) and print their
            # sum
            print(max(arr[i: j + 1]) + min(arr[i: j + 1]))
            sys.exit(0)

