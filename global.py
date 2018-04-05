result1 = 0
result2 = 0


def adder1(num):
    global result1
    result1 += num
    return result1


def adder2(num):
    global result2
    result2 += num
    return result2

def adder3(num):
    result3 = 0
    result3 += num
    return result3


print(adder1(3))
print(adder1(4))
print(adder1(10))
print(adder2(3))
print(adder2(7))

print(adder3(5))
print(adder3(10))
print(adder3(3))

# 전역 변수 (global 선언)의 경우 메서드를 통해 값이 반환될때 값은 계속해서 누적된다.

# 지역 변수 (메서드 내부에 변수 생성)의 경우 메서드를 통해 값이 반환될때 값은 새롭게 반환된다.
