#!/usr/bin/env python3

# initialize a list to store the ranges as tuples
nums = []
# initialize a list to store my ticket numbers
my_ticket = []
# initialize a list to store nearby ticket numbers
nearby_tickets = []

# fetch the input
with open('input.txt', 'r') as f:
    # initialize a flag
    flag = None
    # parse it line by line
    for line in f.readlines():
        # empty line
        if not line.strip():
            # skip
            continue
        # get the first filed
        ff = line.strip().split(':')[0]
        # if the line has ticket field information
        if not flag and ff != 'your ticket' and ff != 'nearby tickets':
            flag = 'info'
        # if it has ticket information
        elif ff == 'your ticket':
            flag = 'my ticket'
        # if it has others tickets information
        elif ff == 'nearby tickets':
            flag = 'nearby tickets'

        if flag == 'info':
            # <field name>: <number range> or <number range>
            # split the line to get the field name and the right side
            field, tmp = line.strip().split(':')
            # split tmp on ' or ' to get two ranges
            nr1, nr2 = tmp.strip().split(' or ')
            # now split two ranges on '-' to get the individual numbres
            n1, n2 = map(int, nr1.split('-'))
            n3, n4 = map(int, nr2.split('-'))
            # append it to the nums list
            nums.append((n1, n2))
            nums.append((n3, n4))
        elif flag == 'my ticket' and ':' not in line.strip():
            # populate the my tickets list
            my_ticket.extend(list(map(int, line.strip().split(','))))
        elif flag == 'nearby tickets' and ':' not in line.strip():
            # populate the nearby tickets list
            nearby_tickets.extend(list(map(int, line.strip().split(','))))

# get the maximum value of the field
max_ = max(max(my_ticket), max(nearby_tickets))
# make an array to denote the indexes that are free
arr = [0] * (max_ + 1)

# fill the arr with the occupied values
for mi, ma in nums:
    # fill the arr values
    for i in range(mi, ma + 1):
        arr[i] = 1

# initialize a empty list to store the invalid ticket fields
invalid = []
# iterate over the ticket fields and check if it's empty
for n in my_ticket:
    if arr[n] == 0:
        invalid.append(n)

for n in nearby_tickets:
    if arr[n] == 0:
        invalid.append(n)

# for the first puzzle
print(sum(invalid))
