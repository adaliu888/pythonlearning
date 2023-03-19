# 摄氏温度转为华氏温度

# 用户输入摄氏温度

# 接收用户输入
sheshidu = float(input('输入摄氏温度: '))

# 计算华氏温度
fahrenheit = (sheshidu * 1.8) + 32
print('%.2f 转化 %.2f' % (sheshidu, fahrenheit))
