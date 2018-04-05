from Class import FourCal

class MoreFourCal(FourCal):

    def pow(self):
        result = self.first ** self.second
        return result

a = MoreFourCal(1,3)

# print(omg.pow())