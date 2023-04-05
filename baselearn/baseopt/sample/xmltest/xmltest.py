from cgi import parse_header
import xml.sax


class MovieHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.CurrentData = "",
        self.type = "",
        self.format = "",
        self.year = "",
        self.rating = "",
        self.stars = "",
        self.description = ""
    # 元素开始调用

    def startElement(self, tag, attributes):
        self.CurrentData = tag
        if tag == "movie":
            print("************movie****************")
            title = attributes["title"]
            print("Title:", title)
    # 元素结束调用

    def endElement(self, tag):
        if self.CurrentData == "type":
            print("type:", self.type)
        elif self.CurrentData == "format":
            print("format:", self.format)
        elif self.CurrentData == "year":
            print("year:", self.year)
        elif self.CurrentData == "rating":
            print("rating:", self.rating)
        elif self.CurrentData == "stars":
            print("stars:", self.stars)
        elif self.CurrentData == "descripion":
            print("descripion:", self.descripion)
        self.CurrentData = ""
    # 读取字符时调用

    def characters(self, content):
        if self.CurrentData == "type":
            self.type = content
        elif self.CurrentData == "format":
            self.format = content
        elif self.CurrentData == "year":
            self.year = content
        elif self.CurrentData == "rating":
            self.rating = content
        elif self.CurrentData == "starts":
            self.stars = content
        elif self.CurrentData == "descripion":
            self.descripion = content
        self.CurrentData = content


if (__name__ == "__main__"):
    # 创建一个xmlreader
    parser = xml.sax.make_parser()
    # 关闭命名空间
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)
    # 重写ContextHandler
    Handler = MovieHandler()
    parser.setContentHandler(Handler)

    parser.parse("movies.xml")
