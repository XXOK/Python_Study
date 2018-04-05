class FourCal:
    def __init__(self,first,second):
        self.first = first
        self.second = second

    # def setdata(self,first,second):
    #     self.first = first
    #     self.second = second

    def sum(self):
        result = self.first + self.second
        return result

    def mul(self):
        result = self.first * self.second
        return result

    def sub(self):
        result = self.first - self.second
        return result

    def div(self):
        print("안녕하세요")

class SafeCal(FourCal):
    def div(self):
        super().div()
        print("제 이름은 강연신입니다.")

a = SafeCal(4,2)

# a.setdata(2,4)

# print(a.sum())
# print(a.mul())
# print(a.sub())