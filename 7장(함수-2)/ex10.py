# 원의 면적과 원의 둘레를 구하는 프로그램을 작성하는데
# PI = 3.141592 전역상수를 선언하고 활용하도록 한다.

# 원의 면적을 구하는 함수를 선언 및 구현
# 원의 면적 공식 : pi * 반지름의 제곱
def circle_Area():
    cca = radius * radius * pi
    print("원의 면적은 ", cca, "입니다.")

# 원의 둘레을 구하는 함수를 선언 및 구현
# 원의 둘레 공식 : 2 * pi * 반지름
def circle_Round():
    ccr = radius * 2 * pi
    print("원의 둘레은 ", ccr, "입니다.")

# 전역 상수를 선언함.
pi = 3.141592
radius = float(input("원의 반지름을 입력하십시오 : "))

circle_Area()
circle_Round()

# 원의 면적과 원의 둘레를 구하는 프로그램을 작성하는데
# PI = 3.141592 전역 상수를 선언하고 상수를 활용하도록 한다.

# 전역 상수를 선언함.
PI = 3.141592
# 프로그램 시작하는 함수
def main():
    radius = float(input("원의 반지름을 입력하세요 : "))
    print("반지름이", radius, "원의 면적 : ", circleArea(radius))
    print("반지름이", radius, "원의 둘레 : ", circleCircumference(radius))


# 원의 면적을 구하는 함수를 선언 및 구현
# 원의 면적 공식 : PI * 반지름의 제곱
def circleArea(radius):
    return PI * radius * radius

# 원의 둘레를 구하는 함수를 선언 및 구현
# 원의 둘레 공식 : 2 * PI * 반지름
def circleCircumference(radius):
    return 2 * PI * radius

# 프로그램의 시작을 알리는 함수 호출
main()