# 第一种方法，执行语句
year = int(input("input first num:"))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("{0}是闰年".format(year))
        else:
            print("{0}不是闰年".format(year))
    else:
        print("{0}是闰年".format(year))

else:
    print("{0}不是闰年".format(year))

# 第二种通过函数的方式，实现调用


def runyear(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print("{0}是闰年".format(year))
            else:
                print("{0}不是闰年".format(year))
        else:
            print("{0}是闰年".format(year))
    else:
        print("{0}不是闰年".format(year))

    return


print(runyear(year))
