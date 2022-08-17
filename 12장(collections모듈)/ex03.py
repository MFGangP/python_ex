# OrderedDict 모듈 이름 그대로 순서를 가지는 딕셔너리 객체이다.
# 원래, 딕셔너리는 순서를 보장하지 않는 객체이다.
# 일반적인 딕셔너리 테스트
dic = {}
dic["a"] = 100
dic["b"] = 200
dic["c"] = 300
dic["d"] = 400
dic["e"] = 500

for k,v in dic.items():
    print(k, v)




