# 命名空间是一个包含了变量名称们（键）和它们各自相应的对象们（值）的字典
var1 = 2000
print(type(var1))
print(id(var1))

var1 = 'string'
print(type(var1))
print(id(var1))


# 一个局部变量和一个全局变量重名，则局部变量会覆盖全局变量
var2 = 200


def test():
    global var2
    print(var2)
    var2 = 333
    print(var2)
    # global var2
    # print(var2) global must piror to name


print(var2)
print(globals(test))


print(dir(test))

print(test.__annotations__)
print(test.__class__)
print(test.__closure__)
print(test.__defaults__)
print(test.__name__)
print(test.__filename__)
