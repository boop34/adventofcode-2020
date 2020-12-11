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

# function to check the adjent seats of a certain seat position
def adjacent_seat_check(row, col, r, c, seats):
    '''
    this fucntion takes row and col value of a seat and checks if all of the
    adjacent seats are empty or occupied in the seats matrix of r rows and c
    columns

    it returns true if the current seat is empty and all the adjacent seats
    are not occupied or if the current seat is occupied and four or more seats
    adjacent to it are also occupied else it returns false
    '''
    # initialize a list to store the tuples of (row, col) of adjacent positions
    adj_pos = []

    # set up the adjacent positions
    # efficient and cleanest way: https://stackoverflow.com/a/56718083
    for x in [-1, 0, 1]:
        for y in [-1, 0, 1]:
            if x == y == 0:
                continue
            if 0 <= row + x < r and 0 <= col + y < c:
                adj_pos.append((row + x, col + y))

    # if the given seat is empty
    if seats[row][col] == 'L':
        # check every adjacent position of the current seat
        for x, y in adj_pos:
            # if the adjacent position is not empty return False
            if seats[x][y] == '#':
                return False
    # otherwise the seat is occupied
    else:
        # initialize the occupied seat counter
        oc = 0
        # check every adjacent position of the current seat
        for x, y in adj_pos:
            # if the current adjacent seat is occupied
            if seats[x][y] == '#':
                # incremet the counter
                oc += 1
        # check if there are 4 or more occupied seat
        if oc < 4:
            return False

    # otherwise return True
    return True


# function to apply the seating rules
def apply_rules(n, r, c, seats):
    '''
    this function takes the seat arrangement matrix of r rowa and c columns
    as an argument and process it with the rules
    1) If a seat is empty (L) and there are no occupied seats adjacent to it,
    the seat becomes occupied
    2) If a seat is occupied (#) and four or more seats adjacent to it are
    also occupied, the seat becomes empty
    based on n it applies the rule i.e if n is odd it applies the first rule
    and if n is even it applies the seond rule

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
                adjacent_seat_check(row, col, r, c, seats):
                new_seats[row][col] = '#'
                # mark that change has occured
                change = True
            # if there is an occupied seat at the current position
            # get the adjacent seat states and if there are >= 4 occupied
            # seats the seat becomes empty
            elif seats[row][col] == '#' and n % 2 == 0 and \
                adjacent_seat_check(row, col, r, c, seats):
                new_seats[row][col] = 'L'
                # mark that change has occured
                change = True
            # for anything else
            else:
                # nothing changes
                new_seats[row][col] = seats[row][col]


    # return the new seats arrangement
    return new_seats, change

# initialize a odd number starting point
n = 1
# make a copy of the original seats
new_seats = seats.copy()

# loop untill no changes occures
while True:
    # apply the rules one after another
    new_seats, change = apply_rules(n, r, c, new_seats)
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

# for the first puzzle
print(occupied_seats)
