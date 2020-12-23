#!/usr/bin/env python3

# 1 million
MILLION = 1000000

# initialize the cups input
cups = [5, 3, 8, 9, 1, 4, 7, 6, 2]
# cups = [3, 8, 9, 1, 2, 5, 4, 6, 7]

# initialize total moves to be done i.e 100
moves1 = 100
moves2 = 10000000

def solve(cups, moves, n):
    '''
    this function takes the cups list and the number of moves to be done on
    that cup list, it also takes the length of the list(n)

    it returns the cups list after all the moves are done
    '''
    # initialize the minimum and maximum labels of the cups
    min_cup, max_cup = min(cups), max(cups)

    # initialize the current cup as the first cup in the list
    curr = 0

    # loop for certain moves
    while (moves := moves - 1) >= 0:
        # current cup label
        curr_label = cups[curr]
        # picked up cup indexes(3 cups immediately clockwise of the
        # current cup)
        picked_up = [(curr + 1) % n, (curr + 2) % n, (curr + 3) % n]
        # store the picked up cup labels
        label1 = cups[picked_up[0]]
        label2 = cups[picked_up[1]]
        label3 = cups[picked_up[2]]
        # pop the picked up cards
        cups.pop((cups.index(curr_label) + 1) % len(cups))
        cups.pop((cups.index(curr_label) + 1) % len(cups))
        cups.pop((cups.index(curr_label) + 1) % len(cups))

        # initialize a destination index
        dst = -1
        # initialize the destination cup label i.e (current cup label - 1)
        dst_label = curr_label - 1
        # select a destination card index
        while dst == -1:
            # look if the destination cup label is outside the picked cups
            try:
                # update the destination index
                dst = cups.index(dst_label)
            # otherewise if it's in the picked up cards
            except ValueError:
                # decrement the current cup label by one
                # but if it goes below the lowest label of the cups set it to
                # highest label of the cups
                dst_label = dst_label - 1 if dst_label > min_cup else max_cup

        # place the picked up cups after the destination cup
        cups.insert((dst + 1) % n, label1)  # first cup
        cups.insert((dst + 2) % n, label2)  # second cup
        cups.insert((dst + 3) % n, label3)  # third cup

        # adjust the current cup index forward
        curr = (cups.index(curr_label) + 1) % n

    # return the final arrangement of the cups
    return cups


# size of the input
n = len(cups)
# get the final arrangement
final = solve(cups.copy(), moves1, n)
# get the index of the '1' labeled cup
idx = final.index(1)
# genetare the solution
sol = ''.join(map(str, final[idx + 1:])) + ''.join(map(str, final[:idx]))
# for the first puzzle
print(sol)

# for puzzle two the implementation can be significantly fast by implementing a
# linked list and makeing it circular

# cup class
class Cup:
    def __init__(self, label):
        # initialize the label value
        self.label = label
        # initialize the next pointer
        self.next = None

    # for pretty representation
    def __repr__(self):
        return f'Cup(Label: {self.label}, next:' +\
               f'{self.next.label if self.next else None})'


# function to solve the second puzzle
def solve2(cups, moves, first):
    '''
    this function takes the cups list which contains cup nodes and are part of
    a linked list, it also takes the number of moves to be done and the first
    node of the original cups

    it returns the product of the two nodes immediately clockwise after the cup
    node 1
    '''
    # initialize the current cup as the first cup in the list
    curr = cups[first]

    # loop for certain moves
    while (moves := moves - 1) >= 0:
        # picked up cup indexes(3 cups immediately clockwise of the
        # current cup)
        picked_up = [curr.next, curr.next.next, curr.next.next.next]
        # store the picked up cup labels
        labels = [picked_up[0].label, picked_up[1].label, picked_up[2].label]

        # remove the picked up cup nodes from the list
        curr.next = picked_up[-1].next

        # find the initial destination cup
        # find the destination cup
        dst = curr.label - 1 + (MILLION if curr.label == 1 else 0)
        # ignore the destination cup if it's already picked up
        while dst in labels:
            # decrement the destination value
            dst -= 1
            # if it goes out of the list
            if dst == 0:
                # set it back to the max valued cup
                dst = MILLION

        # insert those three cups
        picked_up[-1].next = cups[dst].next
        cups[dst].next = picked_up[0]

        # update the current node
        curr = curr.next

    # return the multiplication of the two cups next to the cup valued 1
    return cups[1].next.label * cups[1].next.next.label


# initialize a second list to store the Cup object from 1 to 1000000(1 million)
new_cups = [Cup(i) for i in range(MILLION + 1)]

# make the linked list from input cups
for i in range(n - 1):
    # join the cup nodes
    new_cups[cups[i]].next = new_cups[cups[i + 1]]
# join the last remaining cup node from the input
new_cups[cups[-1]].next = new_cups[n + 1]

# now join the the rest of the cup nodes
for i in range(n + 1, MILLION):
    # join the cup nodes
    new_cups[i].next = new_cups[i + 1]
# join the the last cup node ignoring the 0th indexed cup node in new cups
new_cups[-1].next = new_cups[cups[0]]

# for the second puzzle
print(solve2(new_cups, moves2, cups[0]))
