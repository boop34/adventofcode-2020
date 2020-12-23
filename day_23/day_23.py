#!/usr/bin/env python3

# initialize the cups input
cups = [5, 3, 8, 9, 1, 4, 7, 6, 2]
# cups = [3, 8, 9, 1, 2, 5, 4, 6, 7]

# size of the input
n = len(cups)

# initialize the minimum and maximum labels of the cups
min_cup, max_cup = min(cups), max(cups)

# initialize total moves to be done i.e 100
moves = 100

# initialize the current cup as the first cup in the list
curr = 0

# loop for 100 moves
while (moves := moves - 1) >= 0:
    # current cup label
    curr_label = cups[curr]
    # picked up cup indexes(3 cups immediately clockwise of the current cup)
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


# get the final arrangement
final = cups
# get the index of the '1' labeled cup
idx = final.index(1)
# genetare the solution
sol = ''.join(map(str, final[idx + 1:])) + ''.join(map(str, final[:idx]))
# for the first puzzle
print(sol)
