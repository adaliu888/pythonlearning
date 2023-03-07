counter = 100  # inter型
print(type(counter))
print(id(counter))
counter = counter + 1
print(type(counter))
print(id(counter))

miles = 1000.0  # float型

name = "runoob"  # "字符串型"

print(counter, miles, name)

# 多个变量赋值
a = b = c = 3

print(a, b, c)

a, b, c = 1, 2, "runoob"

print(a, b, c)

a, b, c, d = 20, 5.5, True, 4+3j

print(a, b, c, d)

print(type(a), type(b), type(c), type(d))

a = 111
print(isinstance(a, int))
# type()不会认为子类是一种父类类型，可以用来查询变量所指的对象类型
# isinstance()是来判断的


class A:
    pass


class B(A):
    pass


print(isinstance(A(), A))

print(type(A()) == A)

print(isinstance(B(), A))

print(type(B()) == A)


print(issubclass(bool, int))

a = [1, 2, 3, 4, 5]
print(a[0])
print(a[2:5])
print(a*2)
print(a[2:])


def reverseword(input):
    inputWords = input.split(' ')
    print(inputWords)

    # 翻转字符串
    inputwords = inputWords[-1:]
    print(inputwords)
    inputWords = inputWords[:-1]

    print(inputWords)
    output = ' '.join(inputWords)
    return output


if __name__ == '__main__':
    input = 'I like python'
    rw = reverseword(input)
    print(rw)
# tuple0(元组)
tuple0 = ('abcd', 'runoob', 'google', 123, 789, 70.2)
tinytuple0 = (123, 'runoob')

print(tuple0)

print(tuple0[0])

for x in tuple0:
    print(x)

print(tuple0 * 2)

print(tuple0 + tinytuple0)
print(tuple0[1:2])


# 集合，类型一样的，长度可以变

sites = {}
print(sites)
sites = set()
print(sites)
sites = {'abd', 123}
print(sites)
if "gogle" in sites:
    print("gogle in sites")
else:
    print("gogle not in sites")


# 集合运算

a = set("abcdefsddr")
b = set('alarcazam')
print(a)
print(b)
print(a-b)  # 差集
print(b-a)
print(a | b)  # 并集
print(a & b)  # 交集
print(a ^ b)  # a和b中不同时存在的元素


# maping

dict = {}
dict['one'] = "1-who?"
dict[2] = "2-am"
print(dict)
tinydict = {"name": "runoob", "code": 1, "sit": "www.runoob.com"}
print(dict["one"])
print(dict[2])
print(tinydict.keys())
print(tinydict.values())
print(tinydict.items())


for x, y in tinydict.items():

    print(x, y)


a = int('12', 16)
print(a)
a = int('0xa', 16)
print(a)
a = int('10', 8)
print(a)


float(1)
print(float(1))
print(float('123'))
x = 'abc'
print(repr(x))


x = 7
print(eval('3*7'))


def f():
    list1 = ['runoob', 'google', 'baidu', 'sina']
    tuple01 = tuple(list1)
    print(tuple01)


if __name__ == '__main__':
    input = 'I like python'
    rw = reverseword(input)
    print(rw)
    f()
