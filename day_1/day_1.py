#!/usr/bin/env python3

from input import arr

# make a dictionary of the iputs to do a O(1) lookup
ip_dict = {i: True for i in arr}

# two numbers that add upto 2020
for i in arr:
    if ip_dict.get((2020 - i), False) and i != (2020 - i):
        # print(f"{i} * {2020 - i}: {(2020 - i) * i}")
        print((2020 - i) * i)
        break

# make a dictionary that stores the sum of every possible pair and store their
# product in the value
pair_dict = {}

for i in range(len(arr) - 1):
    for j in range(i, len(arr)):
        pair_dict[arr[i] + arr[j]] = arr[i] * arr[j]

# three numbers that add upto 2020
for i in arr:
    # for i not to be present in the (2020-i) sum, (2020-i-i) must not be
    # present in the input dict
    if pair_dict.get((2020 - i), False) and \
        not ip_dict.get((2020 - i - i), False):

        print(pair_dict[2020 - i] * i)
        break

