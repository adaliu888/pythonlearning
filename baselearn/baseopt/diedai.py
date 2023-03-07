# 迭代是Python最强大的功能之一，是访问集合元素的一种方式。
# 迭代器是一个可以记住遍历的位置的对象。
# 迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束。迭代器只能往前不会后退。
# yield
# iter() 迭代器，只能前进不能后退，每次调用，从上次的断点开始执行

list1 = [1, 2, 3, 4]
print(iter(list1))

it = iter(list1)

for x in it:
    print(x)  # 此输出与print(next(it)) 导致异常

print(type(it))
ls = 'hello,world!'
itt1 = iter(ls)
print(type(itt1))
print(next(itt1))

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
