# 문제 : data_list = [(90, 80),(85, 75),(90, 100)] 튜플을 원소로 하는
# 리스트를 활용하여 학생의 총점과 평균(소수 첫째자리)을 출력하는 프로그램을
# 작성하시오.
# enumerate() 함수를 이용한다.
# 출력결과
# 1번 학생의 총점은 170점이고 평균은 85.0입니다.
# 1번 학생의 총점은 160점이고 평균은 80.0입니다.
# 1번 학생의 총점은 190점이고 평균은 95.0입니다.

data_list = [(90, 80),(85, 75),(90, 100)]
# enumerate() 함수의 역할 : 반복문 사용 시 몇 번째 반복을 확인할 때 사용을 한다.
hap = 0
avr = 0
for i, score in enumerate(data_list, start=1):
    hap = data_list[i-1][0] + data_list[i-1][1]
    avr = (data_list[i-1][0] + data_list[i-1][1])/2
    print("{}번째 학생의 총점은 {}점이고 평균은 {}입니다.".format(i,hap,avr))

for i, scores in enumerate(data_list):
    hap = 0
    # 학생 1명씩 점수를 누적 시킴
    for score in scores:
        hap += score
    print("%d번 학생의 총점은 %d이고, 평균은 %0.1f입니다." %(i+1, hap, hap/2.0))