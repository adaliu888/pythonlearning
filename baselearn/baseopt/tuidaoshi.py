# python 推导式是一种独特的数据处理方式，可以从一个数据序列构建另一个新的数据序列的结构体
# python 支持各种数据结构的推导式：
# list
# dict
# set
# tuple
names = ['Bob', 'Tom', 'alice', 'Jerry', 'Wendy', 'Smith']
new_names = [name.upper() for name in names if len(name) > 3]
print(new_names)

result = [i for i in range(30) if i % 3 == 0]
print(result)

re2 = [i for i in range(30) if i % 2 == 0]
print(re2)
# list()
listdemo = ['Google', 'Runoob', 'Taobao']
newdict = {key: len(key) for key in listdemo}
print(newdict)
# dict()
dic = {x: x**2 for x in (2, 4, 6)}
print(dic)
# set()
s = {x for x in 'adbdeeesdcc' if x not in 'abc'}
print(s)

# tuple
a = (x for x in range(1, 10))
print(a)
print(tuple(a))
