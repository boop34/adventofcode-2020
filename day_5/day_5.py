#!/usr/bin/env python3

# recursive function to get the boarding pass row and cloumn information
def _get_rowcol(l, h, bp, val):
    '''
    this function takes lower bound(l), upper bound(h) and a boarding pass(bp)
    containing a string
    boarding pass may contain the letters {'F', 'B', 'R', 'L'}
    F -> front / lower half of the row
    B -> back / upper half of the row
    L -> left / lower half of a column
    R -> right / upper half of a column

    returns the seat row and column information for the given boarding pass
    '''

    # base case
    if len(bp) == 0:
        return val

    # get the half of the middle value between upper and lower bound
    mid = (h + l) // 2

    # for letter 'F' or 'L'
    if bp[0] == 'F' or bp[0] == 'L':
        return _get_rowcol(l, mid, bp[1:], l)
    # for the letter 'B' or 'R'
    if bp[0] == 'B' or bp[0] == 'R':
        return _get_rowcol(mid + 1, h, bp[1:], h)

# function to get the seat ID from a given boarding pas
def get_id(bp):
    '''
    wrapper function of the recursive _get_rowcol() function that takes a
    boarding pass and extracts the row and column information

    returns seat ID for the given boading pass
    '''
    # first 7 characters represents a row number between 0 and 127
    row = _get_rowcol(0, 127, bp[:7], 0)
    # last 3 characters represents a clumn number between 0 and 7
    col = _get_rowcol(0, 7, bp[-3:], 0)

    # the seat ID is derived from the seat row and column by the formula
    # seat_ID = row * 8 + col
    return row * 8 + col

# initialize the highest seat ID
max_ID = 0
# initialize a dictionary to store the seat ID's from the input list
seat_dict = {}

# fetch the input boarding passes
with open('input.txt', 'r') as f:
    # read the boarding pass values in each line
    for bp in f.readlines():
        # get the seat ID for the current boarding pas
        seat_ID = get_id(bp.strip())
        seat_dict[seat_ID] = True
        max_ID = max(max_ID, seat_ID)

# first puzzle
print(max_ID)

# find the missing seat_ID(s) in the range [0*8+0]=0 to [127*8+7]=1023
# although our seat isn't at the very front or the very back
# but our_ID + 1 and our_ID - 1 is present on the list
for i in range(8, 1024 - 7):
    if not seat_dict.get(i, False) \
        and seat_dict.get(i + 1, False) and seat_dict.get(i - 1, False):

        print(i)

