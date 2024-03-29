# deque와 list의 성능 테스트 비교
from collections import deque
import time     # 성능 테스트를 하기 위해 time 모듈을 가지고 옴

# 저장 성능 테스트
# 아무런 요소가 없는 deque를 생성함
deque_test = deque()
start = time.time()      # 시작 시간을 저장(second 단위)

for i in range(10000000):
    deque_test.append(i)

end = time.time()
print("deque append 시간 : ", end - start)

# 빈 리스트를 생성함
list = list()
start = time.time()      # 시작 시간을 저장(second 단위)

for i in range(10000000):
    list.append(i)

end = time.time()
print("list append 시간 : ", end - start)

print("-------------------------------")

# 추출 기능 테스트
#
#
# start = time.time()      # 시작 시간을 저장(second 단위)
#
# for i in range(100000000):
#     deque_test.pop()
#
# end = time.time()
# print("deque pop 시간 : ", end - start)
#
# start = time.time()      # 시작 시간을 저장(second 단위)
#
# for i in range(100000000):
#     list.pop()
#
# end = time.time()
# print("list pop 시간 : ", end - start)


start = time.time()      # 시작 시간을 저장(second 단위)

for i in range(10000000):
    deque_test.popleft()

end = time.time()
print("deque popleft 시간 : ", end - start)

start = time.time()      # 시작 시간을 저장(second 단위)

for i in range(10000000):
    list.pop(0)

end = time.time()
print("list pop(0) 시간 : ", end - start)

# 결론은 list, deque를 성능테스트 해보니 데이터를 추가 할 때는
# deque가 훨씬 좋은 성능을 발휘한다. 또한 대용량일수록 더욱 더 많은 차이를
# 나타낸다. 중간에 삽입하는 기능 역시 deque가 훨씬 빠르다라는 것이다.
# 추출할 때는 역시 deque가 list보다 훨씬 빠른 성능을 보인다.
# 데이터 용량이 크면 클수록 deque를 사용을 하는 것을 고려해 봐야한다.