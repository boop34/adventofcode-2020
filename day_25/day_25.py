#!/usr/bin/env python3

# card's public key
card_publ = 10604480
# card_publ = 5764801
# door's publ key
door_publ = 4126658
# door_publ = 17807724

# function to transform the number
def transform(memo, loop_size, subj_num=7, num=1):
    '''
    this function takes a number(initially 1) and trandforms it according to
    the rules for a number of loops given as loop_size

    it returns the transformed number
    '''
    # check if the previous loop size has already been calculated
    if subj_num == 7 and memo.get(loop_size - 1):
        return (memo[loop_size - 1] * subj_num) % 20201227
    # loop for loop_size
    for _ in range(loop_size):
        # set the value of the number itself multiplied by the subject number
        num *= subj_num
        # set the value of the number to the remainder after dividing the value
        # by 20201227
        num %= 20201227

    # return the transformed number
    return num


# initialize a dictionary to store the the transformed numbers and the loop
# sizes
memo = {}

# initialize a initial loop size to 0
ls = 0
# initialize the card's loop size and door's loop size
door_ls, card_ls = None, None

# perform the loop untill both the card's and door's public keys are discovered
while True:
    # increment the loop_size
    ls += 1
    # get the transformed number
    transformed_num = transform(memo, ls)
    # check if it matches the card's public key
    if transformed_num == card_publ:
        # store the loop size
        card_ls = ls
    # check if it matches the door's public key
    if transformed_num == door_publ:
        # store the loop size
        door_ls = ls
    # store the transformed num
    memo[ls] = transformed_num
    # check if both public keys are discovered
    if card_ls and door_ls:
        # break out
        break

# get the encryption key
en_key1 = transform(memo, door_ls, card_publ)
en_key2 = transform(memo, card_ls, door_publ)
# they have to be same
assert en_key1 == en_key2

# solution of the puzzle
print(en_key1)

