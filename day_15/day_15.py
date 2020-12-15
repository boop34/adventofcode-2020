#!/usr/bin/env python3

def solve(n, arr):
    '''
    this function takes a integer n to get the nth element of the series with
    staring number stored in arr

    it returns the nth element
    '''
    # initialize a dictionary to store the last indexes of a number
    l_idx = {}

    # iterate over arr and store the last indexes of the elements in the arr
    for i, v in enumerate(arr):
        # store the index as the value
        l_idx[v] = i

    # adjust the n
    n = n - len(arr)
    # iterate the loop n times
    while (n := n - 1) >= 0:
        # get the lenght of the arr
        i = len(arr)
        # get the last element of the array
        le = arr[-1]
        # check if the number is present in the dictionary
        if l_idx.get(le, -1) != -1:
            # if present then get the difference between the previous index
            # and the last stored index
            arr.append(i - 1 - l_idx[le])
            # update the last index of the current number
            l_idx[le] = i - 1
            if (i - 1 - l_idx[le]) != 0:
                l_idx[i - 1 - l_idx[le]] = i
        else:
            arr.append(0)
            # update the last index of the current number
            l_idx[le] = i - 1

    return arr


# input
arr = [0, 12, 6, 13, 20, 1, 17]
# first puzzle
print(slove(2020, arr)[-1])
# second puzzle TAKES A LOT OF TIME
print(solve(30000000, arr)[-1])
