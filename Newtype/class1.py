class Myclass:
    """一个简单的类实例"""
    i = 12345

    def f(self):
        return 'hello world'


# 实例化类：
x = Myclass()

# 访问类的属性和方法
print("Myclass 类的属性 i 为", x.i)
print("Myclass 类的方法 f 输出为：", x.f())
