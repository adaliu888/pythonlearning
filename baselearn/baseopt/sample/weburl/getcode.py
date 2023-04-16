import urllib.parse
from urllib.request import urlopen
import urllib.request
myurl1 = urllib.request.urlopen("https://www.runoob.com/")
print(myurl1.getcode())  # 获取200
try:
    myurl2 = urllib.request.urlopen("https://www.runoob.com/no.html")
except urllib.error.HTTPError as e:
    if e.code == 404:
        print(404)


myurl = urlopen("https://www.runoob.com")
f = open("runoob_urllib_test.html", 'wb')
content = myurl.read()
f.write(content)
f.close()

encode_url = urllib.request.quote("https://www.runoob.com")  # 编码
print(encode_url)

uncode_url = urllib.request.unquote(encode_url)  # 解码
print(uncode_url)


url = 'https://www.runoob.com/?s='
keyword = 'Python 教程'
key_code = urllib.request.quote(keyword)  # 对请求进行编码
url_all = url+key_code
header = {
    'User-Agent': 'Mozilla/5.0 (X11; Fedora; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}  # 头部信息
request = urllib.request.Request(url_all, headers=header)
reponse = urllib.request.urlopen(request).read()
fh = open("./urllib_test_runoob_search.html", "wb")
fh.write(reponse)
fh.close()
