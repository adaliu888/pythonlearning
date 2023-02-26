# 将序列 s 转换为一个列表
# 元组转化为list
aTuple = (123, 'Google', 'Runoob', 'Taobao')
list1 = list(aTuple)
print(list1)

# 字符串转换成list
str = 'hello python'
list2 = list(str)
print(list2)


# set() 函数创建一个无序不重复元素集，可进行关系测试，删除重复数据，还可以计算交集、差集、并集等。
x = set('runoob')
y = set('google')
print(x, y)
print(x-y)
print(x & y)
print(x ^ y)
print(x | y)

# dict() 函数用于创建一个字典。
# dict语法
dict1 = {}  # 声明字典
dict1 = dict(a='a', b='b', c='c', d='d', e='e',)
print(dict1)
dict2 = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
print(dict2)
# dict3 = dict(zip(['one', 'two', 'three'], [1, 2, 3], [1, 2, 3]))
# print(dict3)
# list3 = [('one', 1), ('two', 2), ('three', 3)]
dict4 = dict([('one', 1), ('two', 2), ('three', 3)])
print(dict4)

# 只使用关键字参数创建字典
number1 = dict(x=2, y=3)
print(number1)
print(type(number1))


empty1 = dict()

print('empty1 = ', empty1)
print(type(empty1))


a = frozenset(range(10))
print(a)


print(chr(0x30), chr(97))

print(ord('a'), ord('\n'))
print(hex(255), hex(65528))
print(type(hex(12)))
print(oct(10))
