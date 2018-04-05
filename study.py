class Zigbang():

    test = "people"

    def setBong(self, a):
        self.test = a
        # setbong 파라미터에 값 입력 시 맨위 test 변수에 저장됨

    def getBong(self):
        return Zigbang.test

if __name__ == '__main__':

    clax = Zigbang()
    clax.setBong("party"+clax.test)

    print(clax.test)
    print(clax.getBong())