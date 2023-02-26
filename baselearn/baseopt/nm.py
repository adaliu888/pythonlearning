# abs(x)返回数字的绝对值，如abs(-10) 返回 10
# fabs返回数字的绝对值，如math.fabs(-10) 返回10.0
import math
a = 10.41
print(abs(a))
print(math.fabs(a))  # import math

print(math.ceil(a))
print(math.floor(a))

b = 10
# print(compile(a, b)) python3已经取消
print(max(1, 2, 3))
print(math.modf(a))

print(math.pow(a, b))
print(round(a, 1))
print(math.sqrt(2))
