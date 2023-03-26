li = ["a", "b", "mpilgrim", "z", "example"]
print(li)  # 打印list

print(li[1])  # 打印第二个元素

print(li[-1])  # 取最后一个值

print(li[-3])  # 从右侧往左侧取值

print(li[1:4])  # 从左侧取第二个值到第三个字符结束


# list增加元素

li.append('new')
print(li)

li.insert(2, 'new')
print(li)

li.extend(['new1', 'new2'])

print(li)

# 搜索list元素
li.index('new')
print(li.index('new1'))

# 删除list元素
li.remove("new")
print(li)
li.pop()
print(li)

# list 运算符

ll = [1, 2]

li = li + ll
print(li)

ll = ll*3
print(ll)

# join list

params = {"server": "mpilgrim", "database": "master",
          "uid": "sa", "pwd": "secret"}

ls = ["%s=%s" % (k, v) for k, v in params.items()]

print(ls)

# ss = ls.join(';') 不是list attribute
# print(ss)
ss = ';'.join(ls)
print(ss)  # 为字符串
print(type(ss))

s = ss.split(';')
print(s)
print(type(s))
