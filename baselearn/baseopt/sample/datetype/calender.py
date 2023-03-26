import calendar

num1 = int(input("yy"))
num2 = int(input("mm"))

print(calendar.month(num1, num2))

monthrange = calendar.monthrange(2023, 2
                                 )
print(monthrange)
