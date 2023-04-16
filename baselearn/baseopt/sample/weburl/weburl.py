from urllib.request import urlopen
myurl = urlopen('http://www.runoob.com/')
print(myurl.read(100))  # 读取网页内容，可以设置读取长度
print(myurl.readline())  # 读取网页行
lines = myurl.readlines()  # 读取网页全部行
for line in lines:
    print(line)  # 打印每一行
