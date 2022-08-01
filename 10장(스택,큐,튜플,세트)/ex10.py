# 부분 집합 연산
set1 = {10, 20, 30}
set2 = {10, 20, 30}
# 2개의 세트가 같은지 검사하는 방법(==, !=)
print("SET1과 SET2가 같은가? : ", set1 == set2)
print("SET1과 SET2가 다른가? : ", set1 != set2)

# 부든호 연산을 이용하여 부분 집한인지 아닌지를 알 수 있는 방법
# 진상위 집합의 개면 : SET2 집합이 SET1 집합에 포함되지만 서로 집합은 동일하지
# 않은 집합을 의미한다.
set1 = {10, 20, 30, 40, 50, 60}
set2 = {10, 20, 30}
# 연산자를 이용한 방법
print("SET2는 SET1의 부분 집합인가? : ", set1 > set2)
# issubset()을 이용한 방법
print("SET2는 SET1의 부분 집합인가? : ", set2.issubset(set1))

# 상위 집합인지 확인하는 방법

# 부등호로써는 확인할 수 있는 방법은 없다.
# print("SET1는 SET2의 부분 집합인가? : ", set1 < set2)
# issuperset()을 이용한 방법
print("SET1는 SET2의 상위 집합인가? : ", set1.issuperset(set2))

# 데이터 값이 집합에 포함되어 있는지 확인하는 방법
Set_String = set("안녕하세요.")
print(Set_String)
if "안" in Set_String:
    print("'안' 문자는 Set_String 세트에 포함되어 있습니다.")

print("------------------------------")
# 집합연산을 할 수 있는 것이 세트라는 자료구조의 장점이다.
# 합집합 : 연산자 | (파이프), union() 메서드를 사용
set1 = {10, 20, 30, 40, 50, 60}
set2 = {10, 20, 30}
print("합집합", set1 | set2)
print("합집합", set1.union(set2))
print("합집합", set2.union(set1))
print("------------------------------")
# 교집합은 두 개의 집합에서 겹치는 요소를 구하는 연산이다.
# 방법 : 연산은 &를 사용하거나 intersection() 이용한다.
set1 = {10, 20, 30, 40, 50, 60}
set2 = {10, 20, 30}
print("합집합", set1 & set2)
print("합집합", set1.intersection(set2))
print("합집합", set2.intersection(set1))
print("------------------------------")
# 차집합은 하나의 집합에서 다른 집합의 요소를 뺴고 남은 집합
# 방법 : 연산자 - 를 사용하거나, difference() 를 사용한다.
set1 = {10, 20, 30, 40, 50, 60}
set2 = {10, 20, 30}
print("차집합", set1 - set2)
print("차집합", set1.difference(set2))
# 차집합을 하고 난 뒤는 아무런 값이 없다.
print("차집합", set2.difference(set1))

# all() 집합에서 모든 값이 참이어야지만 참을 리턴해준다.
# any() 집합에서 값이 하나라도 참이면 참을 리턴해준다.
set1 = {"가나","한국","영국","일본","미국"}
set2 = {10, 0, 0, 0, 0, -7}
print("all()결과 : ", all(set1))
print("all()결과 : ", any(set2))

# 집합이 처음부터 아예 다른지를 확인하고 싶을 때 (같은 요소가 없다.)
print("같은 요소가 없는가 : ", set1.isdisjoint(set2))

# pop()으로 집합의 요소를 제거할 수 있는데, 임의로 아무요소나 삭제한다.
# 단, 정수의 경우는 한번 가져올때의 패턴을 재실행해도 똑같지만, 문자열 타입은
# 삭제 및 출력 패턴이 실행할 때마다 달라진다는 것을 알 수 있다
for _ in range(0, len(set1)):
    print(set1.pop(), end=" ")
print()
print("현재 set1의 크기 : ", len(set1))