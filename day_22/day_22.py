#!/usr/bin/env python3

from collections import defaultdict, deque

# function to play the regular combat game
def regular_combat(p1, p2):
    '''
    this function takes two decks p1 and p2 and determines the winner of the
    game by appling rules of regular combat

    it returns the winner's name and deck
    '''
    # loop untill either one of the decks are empty
    while p1 and p2:
        # check the top card of two decks
        t1, t2 = p1.popleft(), p2.popleft()
        # compare the two card numbers and append the winner's card and looser's
        # card into the winner's deck (cards are never the same valued)
        if t1 > t2:
            p1.extend([t1, t2])
        elif t2 > t1:
            p2.extend([t2, t1])

    # return the winner's name and deck
    return ('p1', list(p1)) if not p2 else ('p2', list(p2))


# initialize a dictionary to store the card configurations
configs = defaultdict(list)

# function to play the recursive combat game
def recursive_combat(p1, p2, game=0):
    '''
    this function takes two decks p1 and p2 and determines the winner of the
    game by appling rules of the recursive combat

    it returns the winner's deck
    '''
    # loop until either one of the decks are empty
    while p1 and p2:
        # first check if the current configuration is already listed and that
        # happened in the current game
        if configs[(tuple(p1), tuple(p2))] == game:
            # player 1 instantly wins
            return ('p1', list(p1))
        # otherwise store the new configurations
        else:
            # store the congiguration with the game number
            configs[(tuple(p1), tuple(p2))] = game

        # get the top cards of each deck
        t1, t2 = p1.popleft(), p2.popleft()
        # get the length of their decks without the top card
        n1, n2 = len(p1), len(p2)

        # check if they have altest as many cards as the value of the top card
        if n1 >= t1 and n2 >= t2:
            # perform regular combat with the number of cards same as the value
            # of the top card
            win, _ = recursive_combat(deque(list(p1)[:t1]),
                                      deque(list(p2)[:t2]), game+1)
            # determine the winner of the round according to the result of the
            # regular combat
            if win == 'p1':
                p1.extend([t1, t2])
            else:
                p2.extend([t2, t1])
        # otherwise one with the higher valued top card wins the round
        elif t1 > t2:
            p1.extend([t1, t2])
        else:
            p2.extend([t2, t1])

    # return the wineer's deck
    return ('p1', list(p1)) if not p2 else ('p2', list(p2))


# function to calculate the score from the deck
def score(deck):
    '''
    this function takes a deck of cards and calculates the score

    it returns a number indicating the score of the deck
    '''
    # initalize a variable to store the score
    score = 0

    # calculate the score
    for i, v in enumerate(deck[::-1]):
        # update the score
        score += v * (i + 1)

    # return the score
    return score


# initialize two players decks as deques (get it? :))
p1 = deque()
p2 = deque()

# fetch the input
with open('input.txt', 'r') as f:
    # get the two decks info
    decks = f.read().split('\n\n')
    # in each decks infomarion first line contains the player number so we
    # ignore that
    p1.extend(list(map(int, decks[0].split('\n')[1:])))
    # ignore the last '\n' while parsing the second deck
    p2.extend(list(map(int, decks[1].split('\n')[1:][:-1])))

# initialize the winner for puzzle 1
_, winner = regular_combat(p1.copy(), p2.copy())

# for the first puzzle
print(score(winner))

# initialize the winner for puzzle 2
_, winner = recursive_combat(p1, p2)

# for the first puzzle
print(score(winner))
