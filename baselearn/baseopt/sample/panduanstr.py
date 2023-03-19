import unicodedata


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        unicodedata.numeric(s)
        turn = True
    except (TypeError, ValueError):
        pass
    return False


print(is_number('foo'))

# 测试字符串和数字
print(is_number('foo'))   # False
print(is_number('1'))     # True
print(is_number('1.3'))   # True
print(is_number('-1.37'))  # True
print(is_number('1e3'))   # True

# 测试 Unicode
# 阿拉伯语 5
print(is_number('٥'))  # True
# 泰语 2
print(is_number('๒'))  # True
# 中文数字
print(is_number('四'))  # True
# 版权号
print(is_number('©'))  # False
