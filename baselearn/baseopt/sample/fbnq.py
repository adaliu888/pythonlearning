

ls = []


def fb(n):
    if n <= 1:
        return n
    else:
        return (fb(n-2)+fb(n-1))


# 获取用户输入：
nterms = int(input("您要输出几项？"))

if nterms < 0:
    print("input zhengshu")
else:
    print("input fbnq list")
    for i in range(nterms):
        ls.append(fb(i))
print(ls)
