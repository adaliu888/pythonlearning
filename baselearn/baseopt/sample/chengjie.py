num = int(input("输入一个数字"))

factorial = 1

if num < 0:
    print("0没有乘介")
elif num == 0:
    print("0的乘介是1")
else:
    for i in range(1, num+1):
        factorial = factorial * i
    print("%d 的乘介 %d", (num, factorial))
