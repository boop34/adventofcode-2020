#!/usr/bin/env python3

import itertools
import re

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
            rule_no, rule = line.strip().split(': ')
            # add the rule to the dictionary
            rules[int(rule_no.strip())] = rule.strip().strip('""')
        # otherwse the line contains received mesages
        else:
            # append the message to the received messages list
            recv_msgs.append(line.strip())

# initialize a dictionary to memoize wihle recursion
memo = {}

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
    # check if the key is already memoized
    if memo.get(key, False):
        # return the value
        return memo[key]

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

    # memoize the key value
    memo[key] = r_vals
    # return the list of all the values of the current rule
    return r_vals


'''
SLOW -> SEE BELOW FOR FAST REGEX SOLUTION
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
'''

# initialize a dictionary to memoize the patterns
memo_regex = {}

# recursive function to generate the regex pattern
def _generate_pattern(key, rules):
    '''
    this function takes the dictionary of rules and based on the given key
    generates a regex pattern

    it returns the regex pattern string
    '''
    # base case
    # check if the key contains a alphabet string
    if rules[key].isalpha():
        # return the string
        return rules[key]
    # check if the key is already memoized
    if memo_regex.get(key, False):
        # return the value
        return memo_regex[key]

    # initialize a pattern list to match the current rule key
    pat = []
    # get the rule
    rule = rules[key]
    # split the rule to get all the part
    parts = rule.split('|')

    # iterate over every part
    for p in parts:
        # initialize a string to generate the current part pattern
        curr_pat = ''
        # split the current part
        rule_keys = map(int, p.strip().split(' '))
        # iterate over every individual rule key
        for rk in rule_keys:
            # append the value of the keys to list of current rule values
            curr_pat +=  _generate_pattern(rk, rules)
        # append the current part pattern into the original rule pattern
        pat.append(curr_pat)

    # join the parts pattern with '|' to simulate the or condition
    pat = '|'.join(pat)
    # wrap the pattern with parenthesis
    pat = '(' + pat + ')'
    # memoize the pattern to the current rule key
    memo_regex[key] = pat
    # return the pattern for the current rule key
    return pat


# function to count the number of valid messages
def count_valid(recv_msgs, pat):
    # initialize the counter
    c = 0

    # iterate over the received messages
    for msg in recv_msgs:
        # check if the pattern matches the msg
        if re.match(pat, msg):
            # increment the count
            c += 1
    # return the count
    return c


# get the regex pattern for the 0 th rule
# wrap the pattern with '^' and '$' to get a full match
pat1 = '^' + _generate_pattern(0, rules) + '$'

# for the first puzzle
print(count_valid(recv_msgs, pat1))

'''
for the second part of the puzzle a couple of rules are changed
from '8: 42' to '8: 42 8' and from '11: 42 31' to '11: 42 31 | 42 11 31'
we don't need to channge the input as it'll generate a infinete recursion
rules[8] = '42 8'
rules[11] = '42 31 | 42 11 31'
rules[0] = '8 11' so we only need the pattern for rule 42 and rule 31
as 42, 31 are not changing or looing they will generate same value

so in regex it is easier to understand
rule is 8 is now 42 repeated one or more times -> 42+ (regex)
rule 11 is divided in the middle so we need to apply 42{x}31{x} that matches
the 42 patterns exactly x times and then the 31 pattern exactly x times
then by incrementing the x we can keep matching the results until we get
0 results or we could generate a pattern for a certain number of time
say 20
'''

# for the second puzzle
# get the rule 42 pattern and rule 31 pattern
pat42, pat31 = memo_regex[42], memo_regex[31]
# initialize a counter to sum up all the matches
c = 0

# iterate over a range of values
# after a while there will be no matches which in this case is -> 4
# but just to make sure we incremented i till 10
for i in range(1, 11):
    # generate the pattern for rule 8 and 11
    pat8 = pat42 + '+'
    pat11 = pat42 + '{%d}' % (i) + pat31 + '{%d}' % (i)
    # now generate the pattern for rule 0
    pat2 = '^' + '(' + pat8 + pat11 + ')' + '$'
    # increment the counter
    c += count_valid(recv_msgs, pat2)

print(c)

