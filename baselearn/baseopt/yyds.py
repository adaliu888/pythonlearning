# yield
# iter() 迭代器，只能前进不能后退，每次调用，从上次的断点开始执行

list1 = [1, 2, 3, 4]
print(iter(list1))

it = iter(list1)
print(next(it))
print(next(it))
print(next(it))
print(next(it))


def gen_generator():
    yield 1


# def get_value():
#    return 1

def gen_example():
    yield 'befor any yield'
    yield 'first yield'
    print('between yield')
    yield 'between yield'
    print('no yield more')


if __name__ == '__main__':
    ret = gen_generator()
    print(ret, type(ret))
    # ret = get_value()
    # print(ret, type(ret))
    ret = gen_example()
    print(next(ret))
    print(next(ret))
    print(next(ret))
