import os
import sys


class fh:

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

