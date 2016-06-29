
print('Hello world!')

bar = 'this thing'

def debug():
    import pdb; pdb.set_trace()

def foo(this_function):
    print("Foo!")
    this_function()

def main():
    print('Main')
    import pdb; pdb.set_trace()
    foo()
    print('Main2')

def _baz():
    print('baz')

if __name__ == '__main__':
    main()