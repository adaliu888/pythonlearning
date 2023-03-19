x = input("input num1:")
y = input("input num2:")
# 使用临时变量
temp = x
x = y
y = temp

print(x, y)

# 不使用临时变量
x, y = y, x
print(x, y)
