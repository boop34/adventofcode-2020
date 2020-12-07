#!/usr/bin/env python3

# initialize the valid password count
first_valid_count = 0
second_valid_count = 0

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
        # check the criteria for first puzzle
        if c >= num1 and c <= num2:
            first_valid_count += 1
        # check the criteria for second puzzle
        if password[num1 - 1] == letter or password[num2 - 1] == letter:
            if password[num1 - 1] == letter and password[num2 - 1] == letter:
                pass
            else:
                second_valid_count += 1

print(first_valid_count)
print(second_valid_count)

