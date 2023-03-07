# num_type, check number's type
class NUM:
    num = input("请输入一个数字")

    print(type(num))

    def __init__(self, num):
        self.num = num
        if num is int:
            print("i am int")
        elif num is float:
            print("i am float")
        elif num is complex:
            print("i am complex")
        return self.num

    def add(self):
        self.num = self.num + 1
        return self.num

    def subtract(self):
        self.num = self.num - 1
        return self.num

    def divide(self):
        self.num = self.num / 2
        return self.num

    def compair(self):
        self.num = self.num
        if self.num > 0 and self.num < 10:
            print("是个数")
        elif self.num < 20 and self.num >= 10:
            print("是10位数")
        else:
            print("是其他数字")


if __name__ == "__main__":
    num = input("请输入一个数字")
    NUM
