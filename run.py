import sys


def hello():
    print("Hello")


class Hello:
    pass


if __name__ == "__main__":
    #    print(sys.path)
    #    sys.path.append(r'''D: \github\pythonlearning\baselearn\baseopt''')
    #    print(sys.path)
    from baselearn.baseopt import mod
    x = mod.foo(['quux', 'corge', 'grault'])
    print(mod.__file__)
    print(x)
    hello()
