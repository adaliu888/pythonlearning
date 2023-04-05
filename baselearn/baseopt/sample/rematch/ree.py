import re
print(re.match('www', 'www.qq.com').span())  # 在起始位置匹配

print(re.match('com', 'www.qq.com'))  # 不在其实位置匹配

line = "Cats are smarter than dogs"

# .*表示任意匹配除换行符（\n、\r）之外的任何单个或多个字符
# (.*?)表示‘非贪婪’模式，只保存第一匹配到的子串

matchObj = re.match(r'(.*) are (.*?) .*', line, re.M | re.I)

if matchObj:
    print("matchObj.group():", matchObj.group())
    print("matchObj.group(1):", matchObj.group(1))
    print("matchObj.group(2):", matchObj.group(2))
else:
    print("No match")

# re.search 扫描整个字符串并返回第一个成功的匹配。
