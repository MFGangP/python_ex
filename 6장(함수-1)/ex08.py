# 디폴트 인수(default argument) 
# 함수의 매개변수가 기본 값을 가지게 하는 방법

# 아래 hello()는 매개변수 2개를 가지지만 디폴트 인수가 있어서 함수 호출시
# name 에 대응되는 인수 값만 가지고도 호출이 가능하다.
def hello(name, msg = "반갑습니다."):
    print("안녕하세요 " + name + ',' + msg)

# name 에 대응되는 매개변수값을 하나만 가지고 함수를 호출함.
hello("은혁님")
# 매개변수 name, msg 는 기본 인수값이 존재하지만, 아래와 같이 매개변수를 직접
# 2개를 인자값으로 제시를 하니깐 기본 인수값은 무시가 된다.
hello("은혁님", "잘 가세요.")