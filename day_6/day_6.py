#!/usr/bin/env python3


def count_everyone(ans, n):
    '''
    this functions takes the dictionary 'ans' that has letter:occurrence as
    the key:value pair and the number of members in the group

    returns the total number of questions that everyone answered 'yes'
    '''
    # initialize a temporary counter
    tmp_c = 0

    # iteratre over the items of the dictionary
    for letter, occurrence in ans.items():
        # check if everyone answered yes to the question
        if occurrence == n:
            tmp_c += 1

    # return the count
    return tmp_c

# initialize the counter to count the total number of questin that ANYONE
# has answered 'yes'
ca = 0

# initialize the counter to count the total number of questin that EVERYONE
# has answered 'yes'
ce = 0

# fetch the inputs
with open('input.txt', 'r') as f:
    # initialize the dictionary to count unique 'yes' answered questions
    ans = {}
    # initialize the number of members of a group
    n = 0
    # read the inputs line by line
    for line in f.readlines():
        # if the line is empty that means every members of the group has
        # answered
        if not line.strip():
            # process the current group
            # increment the count that anyone answered 'yes'
            ca += len(ans.keys())
            # increment the count that everyone said 'yes'
            ce += count_everyone(ans, n)
            # reset the group answer set for the next group
            ans = {}
            # restet the group member count
            n = 0
        # if not empty then read the answers
        else:
            # read the answers of a individual
            tmp_ans = line.strip()
            # add the answers into the set
            for i in tmp_ans:
                ans[i] = ans.get(i, 0) + 1
            # increment the member count
            n += 1

# add the last group's count
ca += len(ans.keys())
ce += count_everyone(ans, n)

# first puzzle
print(ca)
# second puzzle
print(ce)
