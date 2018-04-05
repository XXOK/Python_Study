from kang import Jaevi

class Report(Jaevi):
    def Notice(self):
        print(Jaevi.Rnd(self) + "님이 당첨 되셨습니다.")


notice = Report()

notice.Notice()