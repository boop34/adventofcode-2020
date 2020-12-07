#!/usr/bin/env python3

# function to check validity
def check_validity(fields):
    '''
    fields is a dictionary containg key:value pairs where keys are the valid
    fields and values are the respective information of the fields

    returns if the passport is valid or not
    '''

    # check the 'byr'(birth year) field: must be 4 digits and must be within
    # 1920 to 2002
    if not fields['byr']:
        return False
    try:
        if int(fields['byr']) < 1920 or int(fields['byr']) > 2002:
            return False
    except ValueError:
        return False

    # check the 'iyr'(issue year) field: must be 4 digits and must be within
    # 2010 and 2020
    if not fields['iyr']:
        return False
    try:
        if int(fields['iyr']) < 2010 or int(fields['iyr']) > 2020:
            return False
    except ValueError:
        return False

    # check the 'eyr'(expiration year) field: must be 4 digits and must be
    # within 2020 and 2030
    if not fields['eyr']:
        return False
    try:
        if int(fields['eyr']) < 2020 or int(fields['eyr']) > 2030:
            return False
    except ValueError:
        return False

    # check the 'hgt'(height) field: must be a number followed by cm/in
    # if cm -> the number must be within 150 and 193
    # in in -> the number must be within 59 and 76
    # seperate the height and the unit
    if not fields['hgt']:
        return False
    try:
        h, u = int(fields['hgt'][:-2]), fields['hgt'][-2:]
    except ValueError:
        return False

    if u == 'cm' and (h < 150 or h > 193):
        return False
    if u == 'in' and (h < 59 or h > 76):
        return False
    if u != 'cm' and u != 'in':
        return False

    # cehck the 'hcl'(hair color) field: must be a '#' followed by 6 chars
    # between 0-9 or a-f
    # get the color value, it must be a hex value
    if not fields['hcl']:
        return False
    elif '#' not in fields['hcl']:
        return False
    try:
        hc = int(fields['hcl'][1:], 16)
        if len(fields['hcl'][1:]) != 6:
            return False
    except ValueError:
        return False

    # check the 'ecl'(eye color) field: must be any one of {'amb', 'blu',
    # 'brn', 'gry', 'grn', 'hzl', 'oth'}
    if not fields['ecl']:
        return False
    valid_ec = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    if fields['ecl'] not in valid_ec:
        return False

    # check the 'pid'(passport id) field: must be a 9 digit number including
    # leading 0(s)
    if not fields['pid']:
        return False
    try:
        if (int(fields['pid']) < 0) or (len(fields['pid']) != 9):
            return False
    except ValueError:
        return False

    # if passed all the conditions then the passport is valid
    return True

# initialize the valid passport counter
valid_count = 0

# valid fields names
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

            # if it has 8 fields then it's valid
            if check_validity(fields):
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
if check_validity(fields):
    valid_count += 1

print(valid_count)

