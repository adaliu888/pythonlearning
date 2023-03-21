num = int(input("输入一个数字："))

for i in range(1, num):
    if i > 1:
        if i % 2 == 0:
            print("{0}不是素数".format(i))
        else:
            print("{0}是素数".format(i))

    else:
        print("不是自然数")
