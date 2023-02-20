def fun1(str):
    print(str)
    return 1


fun1("aaa")
fun1("wo yao dayin !")

# 函数结构


def printme(str):
    print(str)
    return 1


printme("hello")


# 带两个参数，其中数字、字符串、tuple为不可变参数，list,dict为可变参数。

def bj(a, b):
    if a > b:
        print(a)
        # print(id(a))
    if a < b:
        print(b)
        # print(id(b))
    if a == b:
        pass


def a1(a):
    # print(a)
    return a


def b1(b):
    # print(b)
    return b


bj(2, 3)
bj("a", "b")
bj(3.0, 2.2)
bj((2, 3), (4, 5))
bj((2, 2), (2, 1))
# bj({1: "a", 2: "b"}, {"a": "apple", "b": "quq"})  not suport dict type
a1(1)
b1(2)
bj(a1(1), b1(2))

# 是否可以传递函数呢？

# 形参和实参取值相同，如果如果重新赋值取的id不同


def changeme(aa):
    print(id(aa))
    aa = 4
    print(id(aa))


aa = 1
print(id(aa))
changeme(aa)


# 传递可变对象实例
def changebb(mylist):
    "修改传递的List"
    mylist.append([1, 2, 3, 4])
    print("函数内取值：",
          mylist)
    return


# 调用changebb函数
mylist = [10, 20, 30]
changebb(mylist)
print("函数外取值：", mylist)

# 必须参数


def printstr(str):
    "print some string"
    print(str)
    return


# printstr(),如果调用的参数为空，报错
printstr("aa")


def cc():  # call type = none type ,不必传参
    pass


cc()

# 行数调用参数不需要指定顺序


def printinfo(name, age):
    "打印任何可以传输的字符串"
    print("name", name)
    print("age", age)
    return


# 调用函数printinfo参数
printinfo(age=50, name="John")
