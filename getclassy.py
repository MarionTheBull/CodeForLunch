#!/usr/bin/env python
# The above line is the shebang line to make a python script/code executable
import os
import sys


class fh(object):

    def __init__(self, filename):
        self.filename = filename
        self.contents = list()

    def read_file(self):

        if not os.path.exists(self.filename):
            print('{0} does not exist!'.format(self.filename))
            sys.exit(1)

        with open(self.filename) as f:
            self.contents = f.readlines()
            #TODO remove line endings

    def write_file(self):

        with open(self.filename, 'w') as f:
            for line in self.contents:
                f.write(line)

    def update_contents(self, index, data):

        self.contents[index] = data

    def add_contents(self, data):

        self.contents.append(data)

    # def delete_file(self):

        # os.remove(self.filename)

# 20160907 decorators, a function that wraps a function.

def mad_decorative(func):

    def dooo():
        print('Decorated!')
        func()
    return dooo

def hello():
    print('hello')

@mad_decorative
def world():
    hello()
    print('world!')

# following line makes the code execute when called directly
if __name__ == '__main__':
    # this is what it executes.
    world()