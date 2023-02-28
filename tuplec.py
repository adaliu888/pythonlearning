
tup3 = 'a', 'b', 'c', 'd'
print(type(tup3))
print(tup3)

# 创建一个空元组
tup1 = ()
print(tup1)

# 访问元组：
tup1 = ('Google', 'Runoob', 1997, 2000)
tup2 = (1, 2, 3, 4, 5, 6, 7)

print("tup1[0]", tup1[0])
print("tup2[1:5]", tup2[1:5])


# 修改元组，元组是不准修改的
tup1 = (12, 34.56)
tup2 = ('abc', 'xyz')
tup4 = tup1+tup2

print(tup4)
# 删除元组，
# del tup4
# print(tup4)

# 元组的运算符：
print(len(tup1))
print(tup1+tup2)
print(tup1*4)
print("google" in tup1)
print(x for x in tup1)

for x in tup1:
    print(x)
