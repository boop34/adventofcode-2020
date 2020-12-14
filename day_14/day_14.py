#!/usr/bin/env python3

# function to apply bitmask
def apply_mask(mask, num):
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


# initialize a memory dictionary to store the value at certain address
memory = {}

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
            memory[addr] = apply_mask(mask, l.strip())

print(sum(memory.values()))
