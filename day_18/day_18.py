#!/usr/bin/env python3

# class to create a different number class
class MyNumber:
    '''
    custom number class with overloaded addition, subtraction and bitwise AND
    operator
    '''

    def __init__(self, val):
        # initialize the value of the number class
        self.val = val

    # make the representation look pretty and understandable
    def __repr__(self):
        return f'MyNumber({self.val})'

    # NOTE: the addition(+) and the subtraction(-) operators have the same
    # precedence and bitwise AND(&) operator has lower precedence than them
    # that's why they are the one overloaded

    # if multiplication(*) operator was overloaded it wouldn't have effected
    # the resultant expression as in the time of parsing the python
    # interpreter would have given the higher precedence to the mul(*)
    # operator

    # overload the addition operator with addition representation
    def __add__(self, other):
        # check if the other is a MyNumber object
        assert type(other) == MyNumber, "Other should be MyNumber object"

        return MyNumber(f'({self.val} + {other.val})')

    # overload the subtraction operator with multiplication representation
    def __sub__(self, other):
        # check if the other is a MyNumber object
        assert type(other) == MyNumber, "Other should be MyNumber object"

        return MyNumber(f'({self.val} * {other.val})')

    # overload the bitwise AND operator with multiplication repressentation
    # for the second part of the puzzle
    def __and__(self, other):
        # check if the other is a MyNumber object
        assert type(other) == MyNumber, "Other should be MyNumber object"

        return MyNumber(f'({self.val} * {other.val})')


# initialize variables to store the summation
s1 = 0
s2 = 0

# fetch the input
with open('input.txt', 'r') as f:
    # parse the input line by line
    for line in f.readlines():
        # initialize emptys list to store all the elements
        exp_list1 = []
        exp_list2 = []
        # parse the current line
        for ele in line.strip():
            # if the current element is a whitespace
            if ele == ' ':
                # skip
                continue
            # if the element is a number
            elif ele.isnumeric():
                # make it an object of the custom MyNumber class and append it
                # into the list
                exp_list1.append(str(MyNumber(int(ele))))
                exp_list2.append(str(MyNumber(int(ele))))
            # if it's a '*'
            elif ele == '*':
                # change it to '-'
                exp_list1.append('-')
                exp_list2.append('&')
            # otherwise it's a valid element
            else:
                # append the elemet to the list
                exp_list1.append(ele)
                exp_list2.append(ele)

        # create the expression string by joining the elements of the list
        # then call eval on it to evaluate
        exp1 = eval(''.join(exp_list1))
        exp2 = eval(''.join(exp_list2))
        # now that we have exp as an MyNumber object we can call eval on it's
        # val to get the evaluation of the original expression
        value1 = eval(exp1.val)
        value2 = eval(exp2.val)

        # add the value to the sum
        s1 += value1
        s2 += value2

# for the first puzzle
print(s1)

# for the second puzzle
print(s2)
