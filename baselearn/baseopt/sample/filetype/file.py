# 写文件
with open("test.txt", "wt") as out_f:
    out_f.write("hello world \ni love this world")

# 读文件
with open("test.txt", "rt") as in_f:
    txt = in_f.read()

print(txt)
