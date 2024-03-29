# OrderDict 모듈 이름 그대로 순서를 가지는 딕셔너리 객체이다.
# 원래, 딕셔너리는 순서를 보장하지 않는 객체이다.
# 일반적인 딕셔너리는 순서를 보장하지 않는게 원래의 딕셔너리다. 왜냐하면
# 딕셔너리는 인덱스가 없기 때문이다.
# 파이썬의 버전이 3.6 이상이 됨으로 일반 딕셔너리가 입력된 순서대로
# 정확하게 출력이 되고 있다. 하지만 파이썬 버전이 2.x에서는 순서가
# 준구난방으로 나오고 있는것을 파이썬 튜터를 통하여 확인해보았다.

dic = {}
dic["a"] = 100
dic["b"] = 200
dic["c"] = 300
dic["d"] = 400
dic["e"] = 500
dic["f"] = 100
dic["g"] = 200
dic["h"] = 300
dic["i"] = 400
dic["j"] = 500
for k, v in dic.items():
    print(k, v)

print("-----------------------------")
# OrderedDict는 딕셔너리의 순서, 동등성 비교를 개선한 모듈이다.
from collections import OrderedDict

dic = OrderedDict()
dic["a"] = 100
dic["b"] = 200
dic["c"] = 300
dic["d"] = 400
dic["e"] = 500
dic["f"] = 100
dic["g"] = 200
dic["h"] = 300
dic["i"] = 400
dic["j"] = 500

for k, v in dic.items():
    print(k, v)