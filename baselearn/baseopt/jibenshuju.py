counter = 100  # inter型

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


issubclass(bool, int)
