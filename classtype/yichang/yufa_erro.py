# python 有两种错误很容易辨识：语法错误和异常
# Python assert(断言)用与判断一个表达式，在表达式条件为false的时候触发异常
# while True

print('hello world')

# print(10*(1/0))  # 0不能作为除数

# print(4+spam*3)  # spam 未定义

# print('2'+2)  # int 不能与str 相加


# try/except
# try : 执行代码
# except :  发生异常执行的代码
while True:
    try:
        x = int(input('请输入一个数字：'))
        break
    except ValueError:
        print("你输入的不是数字")
