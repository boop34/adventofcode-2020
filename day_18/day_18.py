#!/usr/bin/env python3

# class to create a different number class
class MyNumber:
    '''
    custom number class with overloaded addition and subtraction operator
    '''

    def __init__(self, val):
        # initialize the value of the number class
        self.val = val

    # make the representation look pretty and understandable
    def __repr__(self):
        return f'MyNumber({self.val})'

    # NOTE: the addition(+) and the subtraction(-) operators have the same
    # precedence that's why they are the one overloaded

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


# initialize a variable to store the summation
s = 0

# fetch the input
with open('input.txt', 'r') as f:
    # parse the input line by line
    for line in f.readlines():
        # initialize an empty list to store all the elements
        exp_list = []
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
                exp_list.append(str(MyNumber(int(ele))))
            # if it's a '*'
            elif ele == '*':
                # change it to '-'
                exp_list.append('-')
            # otherwise it's a valid element
            else:
                # append the elemet to the list
                exp_list.append(ele)

        # create the expression string by joining the elements of the list
        # then call eval on it to evaluate
        exp = eval(''.join(exp_list))
        # now that we have exp as an MyNumber object we can call eval on it's
        # val to get the evaluation of the original expression
        value = eval(exp.val)

        # add the value to the sum
        s += value

# for the first puzzle
print(s)
