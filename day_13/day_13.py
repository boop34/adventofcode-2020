#!/usr/bin/env python3

# fetch the input
with open('input.txt', 'r') as f:
    # initialize the departure time
    d_time = int(f.readline().strip())
    # get the bus information
    bus_ids = f.readline().strip().split(',')
    # ignore the broken down buses marked by 'x'
    bus_ids = list(map(int, (filter(lambda x: x != 'x', bus_ids))))

def solve1(d_time, bus_ids):
    # loop untill we find the perfect bus
    while True:
        # check if the current departure time can be fulfilled by buses
        for bus in bus_ids:
            # chec if the current departure time is divisable by the bus id
            if d_time % bus == 0:
                return d_time, bus
        # otherwise increment the d_time
        d_time += 1


d_time_, bus_id = solve1(d_time, bus_ids)
print(bus_id * (d_time_ - d_time))
