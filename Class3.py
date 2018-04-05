from Class import FourCal
import mod1

class SafeFourCal(FourCal):
    def div(self):
        if self.second == 0:
            return 0
        else:
            return self.first / self.second
    def safe_sum(self):
        if type(self.first) != type(self.second):
            print("뒤지고 싶습니까?")
        else:
            print(mod1.sum(self.first, self.second))

a = SafeFourCal(10,100)
# print(a.safe_sum())
