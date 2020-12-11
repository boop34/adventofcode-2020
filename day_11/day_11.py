#!/usr/bin/env python3

# initilize the seat arrangement grid matrix
seats = []

# fetch the input
with open('input.txt', 'r') as f:
    # iterate through every line and make the seat grid matrix
    for line in f.readlines():
        # prepare the current row
        tmp = [i for i in line.strip()]
        # append the row to the seat matrix
        seats.append(tmp)

# get the number of rows and columns of the seat arrangement matrix
r, c = len(seats), len(seats[0])

# function to recursively find a nearest seat in each of the 8 adjacent
# positions
def _get_adj_seat(row, col, ir, ic, r, c, seats):
    '''
    this function takes the position (row, col) and checks the seats matrix of
    r rows and c cols to see if the given postion is floor or a seat, if it it
    is a floor then it recursively find the first seat in that directon by
    incrementing row by ir and incrementing column by ic

    returns the position of the first seat in (ir, ic) direction
    '''
    # base cases
    # invalid row
    if row < 0 or row >= r:
        return '.'
    # invlaid column
    elif col < 0 or col >= c:
        return '.'
    # found a seat
    elif seats[row][col] != '.':
        return seats[row][col]

    # otherwise keep going in that direction
    return _get_adj_seat(row + ir, col + ic, ir, ic, r, c, seats)


# function to get the adjacent positions of a certain seat
def get_adj_pos(row, col, r, c, seats, puzzle):
    '''
    this function takes a seat position in (row, col) and a seat matrix of r
    row and c cols and we can specify puzzle argument to solve a perticular
    puzzle i.e first or second

    it returns the adjacent seat positions
    '''
    # initialize a list to store tuples of (row, col) of adjacent positions
    adj_pos = []

    # efficient and cleanest way: https://stackoverflow.com/a/56718083
    # for the first puzzle
    if puzzle == 'first':
        for x in [-1, 0, 1]:
            for y in [-1, 0, 1]:
                if x == y == 0:
                    continue
                if 0 <= row + x < r and 0 <= col + y < c:
                    adj_pos.append(seats[row + x][col + y])
    # for the second puzzle
    elif puzzle == 'second':
        for x in [-1, 0, 1]:
            for y in [-1, 0, 1]:
                if x == y == 0:
                    continue
                if 0 <= row + x < r and 0 <= col + y < c:
                    adj_pos.append(_get_adj_seat(row + x, col + y, x, y, r, c,
                                                 seats))

    # return the list of adjacent positions
    return adj_pos


# function to check the adjent seats of a certain seat position
def adjacent_seat_check(row, col, r, c, seats, puzzle):
    '''
    this fucntion takes row and col value of a seat and checks if all of the
    adjacent seats are empty or occupied in the seats matrix of r rows and c
    columns and we can specify puzzle argument to solve a perticular puzzle
    i.e first or second

    it returns true if the current seat is empty and all the adjacent seats
    are not occupied or if the current seat is occupied and four or more seats
    adjacent to it are also occupied else it returns false
    '''
    # get the adjacent positions
    adj_pos = get_adj_pos(row, col, r, c, seats, puzzle)
    # print(adj_pos)

    # if the given seat is empty
    if seats[row][col] == 'L':
        # check every adjacent position of the current seat
        for pos in adj_pos:
            # if the adjacent position is not empty return False
            if pos == '#':
                return False
    # otherwise the seat is occupied
    else:
        # initialize the occupied seat counter
        oc = 0
        # check every adjacent position of the current seat
        for pos in adj_pos:
            # if the current adjacent seat is occupied
            if pos == '#':
                # incremet the counter
                oc += 1
        # check if there are 4 or more occupied seat
        # for the second puzzle it's 5 or more
        if puzzle == 'first' and oc < 4:
            return False
        elif puzzle == 'second' and oc < 5:
            return False

    # otherwise return True
    return True


# function to apply the seating rules
def apply_rules(n, r, c, seats, puzzle):
    '''
    this function takes the seat arrangement matrix of r rowa and c columns
    as an argument and process it with the rules
    1) If a seat is empty (L) and there are no occupied seats adjacent to it,
    the seat becomes occupied
    2) If a seat is occupied (#) and four or more seats adjacent to it are
    also occupied, the seat becomes empty
    based on n it applies the rule i.e if n is odd it applies the first rule
    and if n is even it applies the seond rule
    we can specify puzzle argument to solve a perticular
    puzzle i.e first or second

    it returns the seats matrix after the rule is applied to all the seats
    simultaneously
    '''
    # initialize a new seat arrangement matrix as the rule gets applied
    # simultaneously
    new_seats = [[0 for _ in range(c)] for _ in range(r)]

    # iniialize that no change has occured
    change = False

    # iterate through every row of the seats matrix
    for row in range(r):
        # iterate through every column of the current row
        for col in range(c):
            # if there is an empty seat at the current position
            # get the adjacent seat states and if there are no occupied seats
            # the seat becomes occupied
            if seats[row][col] == 'L' and n % 2 != 0 and \
                adjacent_seat_check(row, col, r, c, seats, puzzle):
                new_seats[row][col] = '#'
                # mark that change has occured
                change = True
            # if there is an occupied seat at the current position
            # get the adjacent seat states and if there are >= 4 occupied
            # seats the seat becomes empty
            elif seats[row][col] == '#' and n % 2 == 0 and \
                adjacent_seat_check(row, col, r, c, seats, puzzle):
                new_seats[row][col] = 'L'
                # mark that change has occured
                change = True
            # for anything else
            else:
                # nothing changes
                new_seats[row][col] = seats[row][col]


    # return the new seats arrangement
    return new_seats, change


def solve(r, c, seats, puzzle):
    '''
    this function takes the seat arrangement of r rows and c columns and the
    puzzle (first / second)

    it returns the number of occupied seats
    '''
    # make a copy of the original seats
    new_seats = seats.copy()

    # initialize a odd number starting point
    n = 1
    # loop untill no changes occures
    while True:
        # apply the rules one after another
        new_seats, change = apply_rules(n, r, c, new_seats, puzzle)
        # if there is no change that means it has stabilized
        if not change:
            break
        # otherwise increment n
        n += 1

    # count the number of occupied seats
    occupied_seats = 0
    # iterate over every row of the stable seat arrangement
    for i in new_seats:
        # increment the counter
        occupied_seats += i.count('#')

    # return the occupied seat count
    return occupied_seats

# for the first puzzle
print(solve(r, c, seats, puzzle='first'))

# for the second puzzle
print(solve(r, c, seats, puzzle='second'))

