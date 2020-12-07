#!/usr/bin/env python3

from input import arr

# two numbers that add upto 2020
for i in arr:
    if (2020 - i) in arr[i:]:
        print(f"{i} * {2020 - i}: {(2020 - i) * i}")

# three numbers that add upto 2020
