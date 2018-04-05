import random

class Jaevi:
    def Rnd(self):
        list = ["강연신", "최준호", "이의석"]
        return random.choice(list)


if __name__ == "__main__":

    Choice = Jaevi()

    print(Choice.Rnd())