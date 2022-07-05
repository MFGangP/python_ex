# 학생들의 성적을 처리하는 프로그램을 만들기
# 조건 : 사용자로부터 성적을 입력받아서 리스트에 저장한다.
#       성적의 평균을 구하고 해당 점수가 80점 이상 성적을 받은 학생의 수를 출력하다.
# 학생 수는 상수 값으로 STUDENT = 5 를 이용한다.
# 츨력결과
# 성적을 입력하시요 : 10
# 성적을 입력하시요 : 20
# 성적을 입력하시요 : 60
# 성적을 입력하시요 : 70
# 성적을 입력하시요 : 80
# 성적의 평균은 48.0 입니다.
# 80점 이상 성적을 받은 학생은 1명입니다.

def sum(gradeList):
    result = 0
    for i in gradeList:
        result += i
    return result

def len(gradeList):
    cnt = 0
    for i in gradeList:
        cnt += 1
    return cnt

def goodGrade(gradeList):
    aCnt = 0
    fCnt = 0
    for i in gradeList:
        if i >= 80:
            aCnt += 1
        else:
            fCnt += 1
    return aCnt

STUDENT = 5
gradeList = []

for i in range(STUDENT):
    gradeList.append(int(input("성적을 입력하시요 : ")))  # 학생들의 성적을 list에 저장함(append() 이용)

avg = sum(gradeList)/len(gradeList) # 평균을 구함 / 성적 합계
print("성적 평균은 ", avg, "입니다.")
print("80점 이상 성적을 받은 학생은 ", goodGrade(gradeList), "명 입니다.")

