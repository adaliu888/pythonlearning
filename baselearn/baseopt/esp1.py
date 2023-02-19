import calendar
import time

x = time.time()  # 当前时间戳
print(x)

x = time.localtime(time.time())
print(x)

x = time.asctime(time.localtime(time.time()))

print(x)

# x = time.localtime(time.time())

print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

print(time.strftime("%Y-%m-%d", time.localtime()))
print(time.strftime("%H:%M:%S", time.localtime()))
print(time.strftime("%H%M%S", time.localtime()))
print(time.strftime("%a %d %b %Y %H:%M:%S", time.localtime()))
a = "Sat Mar 28 22:24:24 2016"
print(time.mktime(time.strptime(a, "%a %b %d %H:%M:%S %Y")))


cal = calendar.month(2016, 1)
print(r"""以下打印2016年1月日历""")
print(cal)

print(time.clock())
