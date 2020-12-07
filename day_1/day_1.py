#!/usr/bin/env python3

from input import arr

# make a dictionary of the iputs to do a O(1) lookup
ip_dict = {i: True for i in arr}

# two numbers that add upto 2020
for i in arr:
    if ip_dict.get((2020 - i), False) and i != (2020 - i):
        print(f"{i} * {2020 - i}: {(2020 - i) * i}")
        break

# three numbers that add upto 2020
