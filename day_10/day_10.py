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

# function to find the total number of ways to arrange the adapters
def arrange_adapters(arr):
    '''
    this function takes an array(arr) of adapter jolt ratings

    it returns the number of distinct ways to arrange the adapters
    '''
    # make a dictionary to store all the possible ways to arrange the adapters
    # to make the jolt rating possible
    jolts = {i: True for i in arr}

    # include the device adapter jolt into the dict
    device_jolt = max(arr) + 3
    jolts[device_jolt] = True

    # initialize the number of eays to arrange the first 3 jolts
    jolts[1] = 1    # as there is only one way to make a 1 jolt output -> (0, 1)
    jolts[2] = 2    # as there is only one way to make a 2 jolt output -> (0, 1, 2), (0, 2)
    jolts[3] = 4    # as there are 2 ways to make a 3 jolt output -> (0, 1, 2, 3), (0, 1, 3), (0, 2, 3), (0, 3)

    # now check for the other jolts derived from the base three jolts
    for i in range(4, device_jolt + 1):
        # if the jolt is not present in the bags or device ignore it
        if not jolts.get(i, False):
            continue
        # if the jolt is present
        else:
            # add up the previous 3 ways to get to current jolt
            jolts[i] = jolts.get(i - 1, 0) + jolts.get(i - 2, 0) + jolts.get(i - 3, 0)

    # return the maximum number of ways to output device_jolt
    return jolts[device_jolt]

# for the second puzzle
print(arrange_adapters(arr))
