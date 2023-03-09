# num_type, check number's type
class NUM:

    def __init__(self, num):
        self.num = num
        print(type(self.num))
        if self.num is not int:
            self.num = int(self.num)
            print(type(self.num))


r = NUM('23')
print(r.num)
