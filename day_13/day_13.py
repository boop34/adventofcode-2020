#!/usr/bin/env python3

# fetch the input
with open('input.txt', 'r') as f:
    # initialize the departure time
    d_time = int(f.readline().strip())
    # get the bus information
    bus_ids = f.readline().strip().split(',')
    # include the 'x' for the second part of the puzzle
    bus_ids = list((int (i) if i != 'x' else -1) for i in bus_ids)
    # bus_ids = list(map(int, (filter(lambda x: x != 'x', bus_ids))))

def solve1(d_time, bus_ids):
    # loop untill we find the perfect bus
    while True:
        # check if the current departure time can be fulfilled by buses
        for bus in bus_ids:
            # if -1 then skip
            if bus == -1:
                continue
            # chec if the current departure time is divisable by the bus id
            if d_time % bus == 0:
                return d_time, bus
        # otherwise increment the d_time
        d_time += 1
    # ideally the control should never get here
    return None


# for the first puzzle
d_time_, bus_id = solve1(d_time, bus_ids)
print(bus_id * (d_time_ - d_time))

# for the second part we have to implement Chinese Remainder Theorem
# https://en.wikipedia.org/wiki/Chinese_remainder_theorem

# initialize a list to store the remainder and moduli tuple
l = []
# populate the list
for i, r in enumerate(bus_ids):
    # if -1 then skip
    if r == -1:
        continue
    # otherwise valid bus id
    else:
        l.append((r, (r - i) % r))

# store the first moduli and the required value
n, x = l[0]

# https://en.wikipedia.org/wiki/Chinese_remainder_theorem#Search_by_sieving
# https://github.com/woj76/adventofcode2020/blob/main/src/day13.py
# iterate over the the list
for n_, a in l[1:]:
    while True:
        x += n
        if x % n_ == a:
            break
    n *= n_

# for the second puzzle
print(x)
