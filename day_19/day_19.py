#!/usr/bin/env python3

import itertools

# initialize a dictionary to store the rules
rules = {}
# initialize a list to store the received messages
recv_msgs = []

# fetch input
with open('input.txt', 'r') as f:
    # parse it line by line
    for line in f.readlines():
        # check if the current line is empty
        if not line.strip():
            # skip
            continue

        # if the line contains a rule
        if ':' in line.strip():
            # split the line appropriately
            rule_no, rule = line.strip().split(':')
            # add the rule to the dictionary
            rules[int(rule_no.strip())] = rule.strip().strip('""')
        # otherwse the line contains received mesages
        else:
            # append the message to the received messages list
            recv_msgs.append(line.strip())

# recursive function to construct a rule value
def _find_rule(key, rules):
    '''
    this function takes dictionary of rules and constructs the actual value
    of the given key

    it returns the actual string corresponding the key
    '''
    # base case
    # check if the key contains a alphabet string
    if rules[key].isalpha():
        # return the string
        return rules[key]

    # get the rule
    rule = rules[key]
    # split the rule to get all the part
    parts = rule.split('|')
    # initialize a list of all the rule values
    r_vals = []

    # populate the rules list
    for p in parts:
        # initialize a list to store all the current part keys values
        curr_vals = []
        # split the current part
        rule_keys = map(int, p.strip().split(' '))
        # iterate over every individual rule key
        for rk in rule_keys:
            # append the value of the keys to list of current rule values
            curr_vals.append(_find_rule(rk, rules))
        # generate all the possible combinations
        combs = list(itertools.product(*curr_vals))
        # iterate over the combinations
        for comb in combs:
            # join the current conbinations
            curr_val = ''.join(comb)
            # now append the current value to the rule values
            r_vals.append(curr_val)
    # return the list of all the values of the current rule
    return r_vals


# get the the values for rule: 0
valid_msgs = _find_rule(0, rules)

# initialize a counter
c = 0

# check the vlidity of the recieved messages
for msg in recv_msgs:
    # check if the current message is in the valid messages list
    if msg in valid_msgs:
        # increment the count
        c += 1

# for the first puzzle
print(c)
