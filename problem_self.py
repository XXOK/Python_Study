class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def setx(self, x):
        self.x = x

    def sety(self, y):
        self.y = y

    def pointToString(self, point):
        return str(point) + "km"

    def get(self):
        return self.pointToString(self.x) + "," + self.pointToString(str(self.y))

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

if __name__ == '__main__':

    claxx = Point(5,10)
    claxx.move(5, 0)

    if claxx.x >= 5:
        print("검색한 위치는 서울입니다.")
        print("인천을 기준으로 움직입니다, 움직인 위치 값:" + claxx.get())
    else:
        print("검색한 위치는 지방입니다.")
        print("인천을 기준으로 움직입니다, 움직인 위치 값:" + claxx.get())
