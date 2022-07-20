# 성적 처리 프로그램 만들기(2차원 리스트를 이용)
# 주어진 성적
# score = [
#           [100, 100, 100], [20, 20, 20], [30, 30, 30],
#           [40, 40, 40], [50, 50, 50]
#         ]
# 출력결과
# 번호    국어     영어     수학     총점     평균
# ---------------------------------------
#   1     100     100     100     300     100.00
#   2     20      20      20      60      20.00
#   3     30      30      30      90      30.00
#   4     40      40      40      120     40.00
#   5     50      50      50      150     50.00
# ---------------------------------------
# 총점    240     240     240     720     48.00

score = [
           [100, 100, 100], [20, 20, 20], [30, 30, 30],
           [40, 40, 40], [50, 50, 50]
        ]
krTotal = 0 # 국어 총합
enTotal = 0 # 영어 총합
mtTotal = 0 # 수학 총합
total_sum = 0   # 총점 총합
total_avr = 0   # 평균 총합
print("출력결과")
# 출력 상단부
print("번호 국어 영어 수학 총점 평균")
print("----------------------------")
for i in range(len(score)):
    Sum = 0
    avr = 0
    # 번호를 출력하는 부분
    print("%3d" % (i+1), end="\t")
    krTotal += score[i][0]   # 국어 점수 누적
    enTotal += score[i][1]   # 영어 점수 누적
    mtTotal += score[i][2]   # 수학 점수 누적
    total_sum = (krTotal + enTotal + mtTotal)
    for j in range(len(score[i])):
        print(score[i][j], end="\t")
        # 개인별 총점
        Sum += score[i][j]
    print(Sum, end="\t")
    # 개인별 평균
    avr += round(Sum/len(score[i]),2)
    print(avr)
    # 평균 총합
    total_avr += avr
# 전체 평균
total_avr /= len(score)
print("----------------------------")
print("총점 %d\t%d\t%d\t%d\t%.2f" % (krTotal,enTotal,mtTotal,total_sum,total_avr))
