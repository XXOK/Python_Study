class Cal:
    def __init__(self,first,second,third):
        self.first = first
        self.second = second
        self.third = third

    def sum(self):
        return self.first + self.second + self.third

class AnotherCal(Cal):
    def sumplus(self):
        return self.sum() / 2

if __name__ == "__main__":

    test = AnotherCal(1,2,4)

    print(test.sumplus())