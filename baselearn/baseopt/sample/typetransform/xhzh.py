c = input('输入一个字符：')
a = int(input("输入一个ASCII码："))

print(c + " ASCII ", ord(c))
print(a, "对应", chr(a))


def changechr(a, c):
    print(a, "对应", chr(a))
    print(c+" ASCII ", ord(c))


print(changechr(a, c))
