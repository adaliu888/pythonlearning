# num 直接报错
from random import choice, randrange
import random


ls = [1, 2, 3, 4]
print(choice(ls))

print(randrange(2, 16, 3))

print(random.random())


random.seed('e', 2)
print('使用字符生成种子', random.random())
random.seed('e', 2)
print('使用字符生成种子', random.random())
