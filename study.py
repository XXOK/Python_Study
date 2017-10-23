class Zigbang():

    test = "people"

    def setBong(self, a):
        self.test = a

    def getBong(self):
        return Zigbang.test

if __name__ == '__main__':

    clax = Zigbang()
    clax.setBong("party"+clax.test)

    print(clax.test)
    print(clax.getBong())