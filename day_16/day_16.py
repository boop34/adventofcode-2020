#!/usr/bin/env python3

# initialize a list to store field names
fields = []
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
            # append the fields
            fields.append(field)
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
            nearby_tickets.append(list(map(int, line.strip().split(','))))

# get the maximum value of the field
max_ = max(my_ticket)
# check the nearby tickets also
for i in nearby_tickets:
    if max(i) > max_:
        max_ = max(i)

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

for i in nearby_tickets:
    for n in i:
        if arr[n] == 0:
            invalid.append(n)

# for the first puzzle
print(sum(invalid))

# initialize a dictionary to keep track of the fields that a number can be
possible_field_dict = {}

# function to check the possible fields of a ticket number position
def check(l, nums):
    '''
    this function takes a list(l) and a list of tuples (nums) and checks what
    tuples successfully marks the boundary of all the element in the list
    NOTE: in nums two consecutive tuples are related

    it returns a list that holds all the possibility of the list having a
    boundary index
    '''
    # initialize a list
    ret = []
    # iterate over every two tuple pairs
    for j in range(0, len(nums), 2):
        # unpack the consecutive tuples
        mi1, ma1 = nums[j]
        mi2, ma2 = nums[j + 1]
        # det the flag
        f = True
        # iterate over every element of the list
        for i in l:
            # check if the list is in bounds
            if mi1 <= i <= ma1 or mi2 <= i <= ma2:
                pass
            # otherwise break
            else:
                f = False
                break
        # if succsessful then add the index to the list
        if f:
            ret.append(j // 2)
    # return the list
    return ret


# get all the elements by their position
for i, v in enumerate(zip(*nearby_tickets)):
    # filter it so that no invalid numbers gets detected
    l = list(filter(lambda x: x not in invalid, v))
    # populate the dictionary of the possible fields indexes
    possible_field_dict[i] = check(l, nums)

# sort the field dict for easier processing
sorted_list = sorted(possible_field_dict.items(), key=lambda x: len(x[1]))

# initialize a set to store the determined fields
s = set()
# initialize a dictionary to store the actual fields names with their position
field_dict = {}

for i, v in sorted_list:
    # filter the used values
    fl = list(filter(lambda x: x not in s, v))
    # add the new element to the set
    s.add(fl[0])
    # populate the actual field dict
    field_dict[fields[fl[0]]] = i

# initialize a variable to get multiplied
ans = 1

# iterate over the keys of the fictionary
for i in field_dict:
    # if the key has the word 'departure' in it
    if i.startswith('depart'):
        # multiply with my ticket field of that name
        ans *= my_ticket[field_dict[i]]

# for the second puzzle
print(ans)

