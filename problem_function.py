class Function:
    empty = []

    def getmyaverage(self, x, y):
        return (x+y)/2

    def get_max_min(self, data_list):
        max_val = max(data_list)
        min_val = min(data_list)
        return min_val, max_val

    def add_start_to_end(self, start, end):
        return sum(range(start, end+1))

    def getText(self, text_list):
        for i in text_list:
            self.empty.append(i[0:3])
        return self.empty


if __name__ == '__main__' :

    claxx = Function()

    print(claxx.getText(("안녕하세요", "반갑습니다", "수고하세요")))

    print(claxx.add_start_to_end(1,5))

    print(claxx.get_max_min([1,2,3]))