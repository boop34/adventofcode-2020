#!/usr/bin/env python3

# initialize the valid passport counter
valid_count = 0

# valid fileds names
valid_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']

# get the inputs from the txt file
with open('input.txt', 'r') as f:
    # initialize an empty dict to store the required fields
    fields = {i: False for i in valid_fields}
    # read it line by line
    for line in f.readlines():
        # check if the line is empty
        if not line.strip():
            # if empty line encountered that means we got all the fields of
            # the previous passport

            # get the length of the fields list
            print(list(fields.values()))
            n = len(valid_fields) - list(fields.values()).count(False)

            # if it has 8 fields then it's valid
            if n == 8:
                valid_count += 1
            # if it has 7 fields except for 'cid' then it's also valid
            elif n == 7 and not fields['cid']:
                valid_count += 1

            # reset the fields list to process the next passport
            fields = {i: False for i in valid_fields}
        # if the line is not empty
        else:
            # get all the key:value pair(s) from the current line
            pairs = line.strip().split(' ')
            # get the key(s) and append them in the fields list
            for pair in pairs:
                key, value = pair.strip().split(':')
                fields[key.strip()] = value.strip()

# check for the last passport which it not verified in the loop
n = len(valid_fields) - list(fields.values()).count(False)
if (n == 8) or (n == 7 and not fields['cid']):
    valid_count += 1

print(valid_count)
