#!/usr/bin/env python3

# initialize the valid password count
valid_count = 0

# open the input file
with open('input.txt', 'r') as f:
    # read each line
    for line in f.readlines():
        # format: x-x a: password
        # x -> number
        # a -> letter
        # get the policy and the password separated by a ':'
        policy, password = line.strip().split(':')
        # strip the whitespace from the password
        password = password.strip()
        # extract the numbers and letter from policy
        nums, letter = policy.strip().split(' ')
        # get the individual numbers
        num1, num2 = map(int, nums.split('-'))
        # get the count of the policy letter from the password
        c = password.count(letter)
        # check the criteria and increment the valid password count
        if c >= num1 and c <= num2:
            valid_count += 1

print(valid_count)

