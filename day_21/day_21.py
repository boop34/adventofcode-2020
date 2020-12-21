#!/usr/bin/env python3

from collections import defaultdict, Counter

# initialize a list containing tuples of ingredients and allergens
foods = []

# fetch the input
with open('input.txt', 'r') as f:
    # parse it line by line
    for line in f.readlines():
        # split the ingredients and allergens
        ingredients, allergens = line.strip().split(' (')
        # get the allergens ignoring 'contains ' part and the ')' at the end
        allergens = allergens[9: -1]
        # include the ingredients and allergens in the foods
        foods.append((ingredients, allergens))


# set of unique allergens
u_al = set()

# iterate over the allergens strings
for i, a in foods:
    # extract the individual allergens
    for al in a.split(', '):
        # insert the allergen into the unique allergen set
        u_al.add(al)

# initialize a counter of all the ingredients
ing_counter = Counter()

# iterate over the ingredients to populate the counter
for ingredients, _ in foods:
    # get the list of individual ingredient
    for i in ingredients.split():
        # update the counter
        ing_counter[i] += 1

# initialize a dictionary to store all the possible ingrident lists
possible_alin = defaultdict(list)

# iterate over the unique allergens
for al in u_al:
    # iterate over the foods
    for f in foods:
        # extract the ingredient and allergens set
        ingredients = f[0].split()
        allergens = f[1].split(', ')
        # check if the current unique allergen is present in the current food
        if al in allergens:
            # append the list of ingredients of the current food into the
            # possible allergen ingredient dictionary
            possible_alin[al].append(ingredients)

# initialize a dictionary to store the reduced list of the possible ingredients
# per unique allergen
reduced_dict = {}

# get the intersections per unique allergen
for al in u_al:
    # get the intersection
    tmp = set(possible_alin[al][0]).intersection(*possible_alin[al][1:])
    # include in the dictionary
    reduced_dict[al] = list(tmp)

# sort the items of the dictionary according to the length of the possible
# ingredients to get the better representation
sorted_ing = sorted(reduced_dict.items(), key=lambda x: len(x[1]))

# final allergen dict to store the ingredients that correspond to the allergen
final_al = {}

# loop untill the final allergen dict is filled all the way
while len(final_al) != len(u_al):
    # iterate over the allergens and their ingredients
    for al, ing in sorted_ing:
        # check if the allergen is not already assigned and then length of it's
        # ingredient is 1
        if not final_al.get(ing[0], False) and len(ing) == 1:
            # assign the ingredient to the allergen
            final_al[ing[0]] = al
            break

    # get rid of all the occurences of the just assigned ingredient
    for al_, ing_ in sorted_ing:
        # check if they are not the same
        if al == al_:
            # skip
            continue
        # check if the just assigned ingredient is present in the current
        # ingredient list
        if ing[0] in ing_:
            # remove the occurence
            ing_.remove(ing[0])

# initialize a variable to store the sum
s = 0
# iterate over the ingredients counter
for ing in ing_counter:
    # check if it is not a allergen
    if not final_al.get(ing, False):
        # add the occurence counter
        s += ing_counter[ing]

# for the first puzzle
print(s)
