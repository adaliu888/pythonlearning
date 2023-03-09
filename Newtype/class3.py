#

# 类的定义

class people:
    # 定义基本基础
    name = ''
    age = 0
    # 定义私有属性，私有属性在类的外部无法直接进行访问
    _weight = 0
    # 定义构造方法

    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        self._weight = w

    def speak(self):
        print("%s 说：我 %d 岁。" % (self.name, self.age))


class student(people):
    grate = ''

    def __init__(self, n, a, w, g):
        # 调用父类的构涵
        people.__init__(self, n, a, w)
        self.grate = g
    # 覆写父类的方法

    def speak(self):
        # return super().speak() #调用父类的方法，用super()
        print("%s 说：我 %d 岁,我在读 %d 年级" % (self.name, self.age, self.grate))


class speaker():
    topic = ''
    name = ''

    def __init__(self, n, t):
        self.name = n
        self.topic = t

    def speak(self):
        print("%s,%s", (self.name, self.topic))


class simple(speaker, student):
    a = ''

    def __init__(self, n, a, w, g, t):
        student.__init__(self, n, a, w, g)
        speaker.__init__(self, n, t)


# 实例化类
p = people('runoob', 10, 30)
p.speak()

s = student('ken', 10, 60, 3)
s.speak()

test = simple("tim", 25, 80, 4, "python")
test.speak()
