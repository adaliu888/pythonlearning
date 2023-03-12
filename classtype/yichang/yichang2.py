import sys

try:
    f = open("myfile.txt")
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error:{0}.format(err)")
except ValueError:
    print("Could not convert data to an integer.")
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise


for arg in sys.argv[1:]:
    try:
        f = open(arg, "r")
    except IOError:
        print("Could not open", arg)
    else:
        print(arg, 'has', len(f.readlines()), 'lines')
        f.close()

#


def runoob():
    print("this is runoob")
# 是 try finally可以用来释放资源


try:
    runoob()
except AssertionError as error:
    print(error)
# 嵌套错误提示
else:
    try:
        with open('file.log') as file:
            read_data = file.read()
    except FileNotFoundError as fnf_error:
        print(fnf_error)
# 无论异常是否发生都会执行代码
finally:
    print('这句话，无论异常是否发生都会执行。')
