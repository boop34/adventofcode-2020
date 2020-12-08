#!/usr/bin/env python3

# initialize a list to store all the instructions
instructions = []

# fetch the input
with open('input.txt', 'r') as f:
    # store the instructions
    instructions = f.readlines()

# fucntion to parse the instruction and does the required operation
def execute(i_ptr, acc, instruction):
    '''
    this function takes the instruction pointer(in this case line number),
    instruction string and the accumulator and executes the operation

    updates and returns the accumulator and the next instruction pointer
    '''

    # split the instruction into operation and operand
    operation, operand = instruction.strip().split(' ')
    # convert the operand from string to integer
    operand = int(operand)

    # if the operation is 'acc': increases/decreases the accumulator value
    # with the operand
    if operation == 'acc':
        # update the accumulaor value
        acc += operand
    # if the operation is 'jmp': jumps to a new instruction pointer
    elif operation == 'jmp':
        return i_ptr + operand, acc

    # update the instruction pointer
    return i_ptr + 1, acc

# get the total number of instructions
n = len(instructions)

def check_acc(n, instructions):
    # initialize the instruction pointer at the start
    i_ptr = 0
    # initialize the accumulator to 0
    acc = 0
    # initialize a dictionary to check if a instruction is repeated
    i_dict = {}

    # run the loop until end of instructions
    while i_ptr < n:
        # execute the operation and get the next instruction pointer
        i_ptr, acc = execute(i_ptr, acc, instructions[i_ptr])
        # check if the next instruction is executed before
        if i_dict.get(i_ptr, False):
            break
        # otherwise insert the instruction into the i_dict
        i_dict[i_ptr] = True

    # return the accumulator value
    return acc


# print the accumulator value
print(check_acc(n, instructions))

