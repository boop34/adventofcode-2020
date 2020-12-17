#!/usr/bin/env python3

import itertools

# function to apply bitmask
def apply_mask1(mask, num):
    '''
    this function takes a mask of 36 characters and pllies that to the integer
    num

    it returns a integer after appling the mask
    '''
    # convert the input integer into a binary of 36 length with 0 padding
    b = [i for i in f'{int(num):036b}']

    # get the bits from the mask to change
    bit_mask = {}

    # populate the bit mask
    for i, v in enumerate(mask):
        # check if the value isn't 'X'
        if v != 'X':
            bit_mask[i] = v

    # apply the bit mask
    for idx in bit_mask:
        # replace the index of the binary representation of the integer with
        # the mask value
        b[idx] = bit_mask[idx]

    # return the integer form of the masked binary
    return int(''.join(b), 2)


# function to apply bitmask for the second puzzle
def apply_mask2(mask, num):
    '''
    this function takes a mask of 36 characters and pllies that to the integer
    num

    it returns a integer after appling the mask
    '''
    # convert the input integer into a binary of 36 length with 0 padding
    b = [i for i in f'{int(num):036b}']

    # get the bits from the mask to change
    bit_mask = {}

    # populate the bit mask
    for i, v in enumerate(mask):
        bit_mask[i] = v

    # apply the bit mask
    for idx in bit_mask:
        # If the bitmask bit is 0, the corresponding memory address bit
        # is unchanged
        if bit_mask[idx] == '0':
            continue
        # If the bitmask bit is 1, the corresponding memory address bit
        # is overwritten with 1
        # If the bitmask bit is X, the corresponding memory address bit
        # is floating
        else:
            b[idx] = bit_mask[idx]

    # number of floating bits
    n = b.count('X')

    # generate every possible combination for n number of floating bits
    combinations = list(itertools.product([0, 1], repeat=n))

    # initialize a list to store all the possible numbers generated after
    # handling floating bits
    nums = []

    # iterate over every combination
    for combination in combinations:
        # make a copy of the original masked number
        b_tmp = b.copy()
        # iterate over the individual values of the combination
        for i in combination:
            # now check the number
            for j in range(len(b_tmp)):
                # if a floating bit is found
                if b_tmp[j] == 'X':
                    # replace it with the combination bit
                    b_tmp[j] = str(i)
                    break
        # after all the floating bits are replaced
        nums.append(int(''.join(b_tmp), 2))

    # return the list of possible numbers
    return nums



# initialize a memory dictionary to store the value at certain address
memory1 = {}
# initialize a memory dictionary to store the value at certain address
memory2 = {}

# fetch the input
with open('input.txt', 'r') as f:
    # read it line by line
    for line in f.readlines():
        # get the right side and left side of the '=' sign
        r, l = line.strip().split('=')
        # if right side is 'mask'
        if r.strip() == 'mask':
            # change the mask value
            mask = l.strip()
        # otherwise there is a memory address in the right side
        else:
            # get the address
            addr = int(r.strip().split('[')[1][:-1])
            # fill the memory address by the number after appling the mask
            memory1[addr] = apply_mask1(mask, l.strip())
            # get the posswible memory addresses for second puzzle
            nums = apply_mask2(mask, addr)
            # now fill memory2 with the addresses
            for num in nums:
                # fill the address with the value
                memory2[num] = int(l.strip())

# for the first puzzle
print(sum(memory1.values()))

# for the second puzzle
print(sum(memory2.values()))
