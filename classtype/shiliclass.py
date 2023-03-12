
class user:
    username = 'un'
    password = 'pw'

    def __init__(self, username, password):
        self.a = 1
        self.b = 2

    def fn(ss):
        s = ss
        print(s)


x = user
print(type(x))
print(x.username, x.password)
x.fn("class")
# print(x.a, x.b)
y = user("", "")
print(type(y))
print(y.a, y.b)
# y.fn("instance")
