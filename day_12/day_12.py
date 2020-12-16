#!/usr/bin/env python3

# class for the ferry
class Ferry:
    def __init__(self):
        # initialize the staring position of the ferry
        self.pos = (0, 0)
        # initialize the satring direction the ferry is facing
        self.dir_ = 'E'
        # initialize the starting angle of the ferry
        self.angle = 0
        # initialize a dictionary to represent an angle into a direction
        self.dir_dict = {0: 'E', 90: 'N', 180: 'W', 270: 'S'}
        # initialize the list of movements
        self.moves = []
        # initialize a waypoint
        self.wp = (1, 10)

    def __repr__(self):
        return f'Ferry facing {self.dir_} at the position {self.pos}'

    def fetch_input(self):
        '''
        this function simply fetches the input movements from input.txt and
        updates the movements list
        '''
        # populate the moves list
        with open('input.txt', 'r') as f:
            # parse it line by line
            for line in f.readlines():
                # get the action and the value from the current line
                action, value = line.strip()[:1], int(line.strip()[1:])
                # append the (action, value) tuple into moves list
                self.moves.append((action, value))

    def navigate1(self, moves=None):
        '''
        this function takes a list of tuples(action, value) and applies
        that to navigate the ferry
        '''
        if not moves:
            moves = self.moves
        # iterate over every movement
        for action, value in moves:
            # get the current position and angle of the ferry
            x, y = self.pos
            angle = self.angle

            # if the action is 'F' -> move forward in the current direction
            # by the given value
            if action == 'F':
                # change the action to the current direction
                action = self.dir_

            # if the action is 'N' -> move north by the given value
            if action == 'N':
                # + X-axis movement
                x += value
            # if the action is 'S' -> move south by the given value
            elif action == 'S':
                # - X-axis movement
                x -= value
            # if the action is 'E' -> move east by the given value
            elif action == 'E':
                # + Y-axis movement
                y += value
            # if the action is 'W' -> move west by the given value
            elif action == 'W':
                # - Y-axis movement
                y -= value
            # if the action is 'R' -> turn right by the given angle
            elif action == 'R':
                # clockwise movement
                angle = (360 + angle - value) % 360
            # if the action is 'L' -> turn left by the given value
            elif action == 'L':
                # anti-clockwise movement
                angle = (angle + value) % 360

            # update the ferry position
            self.pos = (x, y)
            # update the ferry direction and angle
            self.angle = angle
            self.dir_ = self.dir_dict[self.angle]

    def navigate2(self, moves=None):
        '''
        this function takes a list of tuples(action, value) and applies
        that to navigate the ferry waypoint
        '''
        if not moves:
            moves = self.moves
        # iterate over every movement
        for action, value in moves:
            # get the current position of the ferry waypoint
            x, y = self.wp

            # if the action is 'F' -> move forward in the current direction
            # by the given value
            if action == 'F':
                # get the current co-ordinates of the ferry
                fx, fy = self.pos
                # change the action to the current direction of waypoint
                fx += value * x
                fy += value * y
                # update the position
                self.pos = (fx, fy)

            # if the action is 'N' -> move north by the given value
            if action == 'N':
                # + X-axis movement
                x += value
            # if the action is 'S' -> move south by the given value
            elif action == 'S':
                # - X-axis movement
                x -= value
            # if the action is 'E' -> move east by the given value
            elif action == 'E':
                # + Y-axis movement
                y += value
            # if the action is 'W' -> move west by the given value
            elif action == 'W':
                # - Y-axis movement
                y -= value
            # if the action is 'R' -> turn right by the given angle
            elif action == 'R':
                # clockwise movement
                for _ in range(value // 90):
                    x, y = -y, x
            # if the action is 'L' -> turn left by the given value
            elif action == 'L':
                # anti-clockwise movement
                for _ in range(value // 90):
                    x, y = y, -x

            # update the ferry position
            self.wp = (x, y)

    def manhattan_dist(self):
        '''
        manhattan distance = east/west pos + north/south pos
        '''
        return abs(self.pos[0]) + abs(self.pos[1])


# for the first puzzle

# initialize the ferry object
f = Ferry()
# fetch the input
f.fetch_input()
# do the navigation
f.navigate1()
# get the manhattan distance
print(f.manhattan_dist())

# for the second puzzle

# initialize the ferry object
f = Ferry()
# fetch the input
f.fetch_input()
# do the navigation
f.navigate2()
# get the manhattan distance
print(f.manhattan_dist())
