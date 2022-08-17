# 일반 딕셔너리를 정렬하여 OrderedDict로 포장하기

dic = {}
dic["b"] = 100
dic["a"] = 200
dic["e"] = 300
dic["d"] = 400
dic["e"] = 500
dic["h"] = 100
dic["j"] = 200
dic["m"] = 300
dic["z"] = 400
dic["x"] = 500
# 키의 값으로 정렬을 해봄
li1 = (sorted(dic.values()))
li2 = (sorted(dic.keys()))
print(li2)
print(li1)
print(dic["j"])

from collections import OrderedDict

# 넘어오는 t의 값은 딕셔너리의 요소이다.
# 하여 0 인덱스는 키 값이 될 것이다.
def sort_by_key(t):
    return t[0]
dic1 = {}
dic1["b"] = 100     # z : 100
dic1["a"] = 200
dic1["e"] = 300
dic1["d"] = 400
dic1["e"] = 500
print("-------------------------")
# 일반 딕셔너리의 내용을 sorted() 를 이용하여 정렬을 하면 키를 기준으로
# 정렬된 리스트가 리턴된다. OrderedDict(0로 포장(Wrapping)을 하고 있다.
# 기존의 딕셔너리나 리스트의 순서를 지키면서 딕셔너리의 형태로 관리를 할
# 수가 있다.
for k, v in OrderedDict(sorted(dic1.items(), key=sort_by_key)).items():
    print(k, v)

# li3 = sorted(dic1.items(), key=sort_by_key)
# print(li3)