# Python 使用 raise 语句抛出一个指定的异常
# raise的语法结构
# raise[Exception[, args[, traceback]]]

# x = 10
# if x > 5:
#    raise Exception('x 不能大于 5。x 的值为: {}'.format(x))


# raise 唯一的一个参数指定了要被抛出的异常，它必须是一个异常的实例或者异常的类

# try:
#   raise NameError('唯一的一个参数指定了要被抛出的异常')
# except NameError:
#    print('An exception flew by!')
#    raise


# 用户自定义异常
class MyError(Exception):
    # 构造函数是始终特殊的方法，主要是对象实例化时初始化类的成员变量
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


try:
    raise MyError(2*2)
except MyError as e:
    print('My exception occurred,value', e.value)
