# 문제 : 아래와 같이 두 개의 세트가 있다. 두 개의 세트에 있는 사람 이름 중에
# 2개의 파티에 모두 참석한 사람은 누구인가를 출력하시오.
# party A에 속하는 사람은 "신은혁", "김연아", "손연재", "김철수"가 있다.
# party B에 속하는 사람은 "최양락", "김기훈", "손연재", "안철수"가 있다.
# 출력결과
# 2개의 파티에 모두 참석한 사람은 아래와 같습니다.
# {'손연재'}

# partyA = {"신은혁", "김연아", "손연재", "김철수"}
# partyB = {"최양락", "김기훈", "손연재", "안철수"}
#
# print("2개의 파티에 모두 참석한 사람은 아래와 같습니다.")
# print(partyA.intersection(partyB))

partyA = {"신은혁", "김연아", "손연재", "김철수"}
partyB = {"최양락", "김기훈", "손연재", "안철수"}
print(partyA)
print(partyB)
print("2개의 파티에 모두 참석한 사람은 아래와 같습니다.")
# print(partyA & partyB)
print(partyA.intersection(partyB))