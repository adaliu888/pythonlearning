
# 2023-02-19,给dict 赋值，关键字重复，值取最后一个
#
from filecmp import cmp


tinydict = {1: "a", 2: 'b'}
print(tinydict)

tinydict = {"adb": 1, 2: 123}
print(tinydict)

tinydict = {"adb": 1, "adb": 123}
print(tinydict)

# 访问字典里的值
tinydict = {1: "a", 2: 'b'}
print(tinydict)
print("tinydict[1] is", tinydict[1])

# 没有的健会报错
# print(tinydict[3])
dict1 = {'Name': 'Zara', 'Age': 7}
dict2 = {'Name': 'Mahnaz', 'Age': 27}
dict3 = {'Name': 'Abid', 'Age': 27}
dict4 = {'Name': 'Zara', 'Age': 7}

seq = ('Google', 'Runoob', 'Taobao')

# 不指定默认的键值，默认为 None
thisdict = dict.fromkeys(seq)
print("新字典为 : %s" % str(thisdict))

# 指定默认的键值
thisdict = dict.fromkeys(seq, 10)
print("新字典为 : %s" % str(thisdict))

# 字典的长度len(dict)
print(len(dict1))

# 字典的类型type()
print(type(dict1))

# 字典可以打印字符串类型str()
print(str(dict1))

print(dict.clear(dict3))
print(dict.copy(dict2))

print(dict1.items())
print(dict1.get('Name'))
# print(dict1.has_key('Name'))  # python3x,不持支这个方法
print(dict2)
print(dict1.keys())
print(dict1.setdefault("sex"))
print(dict1)
print(dict2.update(dict1))
print(dict2, dict1)
print(dict2.values())
print(dict2.popitem())
