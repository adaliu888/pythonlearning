# Filename : exam2.py
# author by : ada liu
# encode = UTF-8

num1 = input("请输入第一个数字：")

num2 = input("请输入第二个数字：")

sum1 = int(num1) + int(num2)

print(sum1)

sum2 = float(num1) + float(num2)
print(sum2)


# 显示打印结果
print('数字{0}和数字{1}相加的结果为：{2}'.format(num1, num2, sum1))
