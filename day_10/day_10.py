#!/usr/bin/env python3

from input import arr

# recursive function to join adapters one after another
def _join_adapter(device_jolt, jolt, jolts, diff):
    '''
    this function takes a jolt value, jolts dictionary which contains all
    the jolts of the adapters in the bag as well as the devices, it also takes
    a diff dictionary that counts the number of 1, 2 or 3 differences occured

    returns the dictionary containing difference distribution
    '''
    # base case if the jolt value is same as device jolt
    if jolt == device_jolt:
        # return the difference dictionary
        return

    # if there is a 1 difference jolt present in the jolts dictionary
    if jolts.get(jolt + 1, False):
        # increment the 1 difference count
        diff[1] = diff.get(1, 0) + 1
        # recursive call
        _join_adapter(device_jolt, jolt + 1, jolts, diff)
    # if there is a 2 difference jolt present in the jolts dictionary
    elif jolts.get(jolt + 2, False):
        # increment the 2 difference count
        diff[2] = diff.get(2, 0) + 1
        # recursive call
        _join_adapter(device_jolt, jolt + 2, jolts, diff)
    # if there is a 3 difference jolt present in the jolts dictionary
    elif jolts.get(jolt + 3, False):
        # increment the 3 difference count
        diff[3] = diff.get(3, 0) + 1
        # recursive call
        _join_adapter(device_jolt, jolt + 3, jolts, diff)


# wrapper function of the recursive _join_adapter() function
def get_difference(arr):
    '''
    this function takes an array(arr) of jolts adapters

    returns the difference distribution of the adapters
    '''
    # make a dictionary to store all the jolts
    jolts = {i: True for i in arr}

    # include the device adapter jolt into the dict
    device_jolt = max(arr) + 3
    jolts[device_jolt] = True

    # initialize the difference dictionary
    diff = {}

    # initialize the starting jolt of the outlate
    starting_jolt = 0

    # call the recursive function
    _join_adapter(device_jolt, starting_jolt, jolts, diff)

    # return the difference dictionary
    return diff

# make the difference dictionary
diff = get_difference(arr)

# for the first puzzle
print(diff[1] * diff[3])

