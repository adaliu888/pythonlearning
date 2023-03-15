# -*- coding: UTF-8 -*-

# Filename : exam3.py
# author by : ada liu

import math
num = float(input("请输入一个数字："))  # 转换程float类型
num_sqrt = num**0.5
print(' %0.3f 的平方根为 %0.3f' % (num, num_sqrt))


num = int(input('输入一个数字：'))
num_sqrt = math.sqrt(num)
print(print('{0} 的平方根为 {1:0.3f}+{2:0.3f}j'.format(num,
      num_sqrt.real, num_sqrt.imag)))
