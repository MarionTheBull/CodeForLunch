import os

def open_file(filename):
    if os.path.exists(filename):
        print('It exists!')
        with open(filename) as f:
            data = f.readlines()
            return data
    else:
        print('{0} does not exist'.format(filename))

