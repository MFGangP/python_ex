# 사용자가 지정하는 파일을 읽어서 파일에 저장되어진 각각의 단어가 몇번이나
# 나오는지 계산하는 프로그램 작성하여 보자.
# 출력결과
# 파일 이름 입력 : words.txt
# {'asia' : 3, 'do' : 2, '신은혁' : 2}

# 파일 이름 입력받기

if __name__ == "__main__":
    word_count = dict() # 빈 딕셔너리를 생성
    f_name = input("입력 파일 이름 : ")
    file = open(file=f_name, mode="r", encoding="utf-8")   # 파일을 열고 읽기 모드로 설정함.

    for line in file:   # 파일로 부터 한 줄 씩 읽는다.
        words = line.split()    # 읽어온 한 줄의 문장을 단어(토큰으로 나눈다.)
        for word in words:      # 단어 리스트에 해당하는 단어만큼 루프를 돈다.
            if word not in word_count:  # 단어가 단어 리스트에 존재하지 아니하면...
                word_count[word] = 1
            else:                       # 존재한다면 값을 증가.
                word_count[word] += 1
    print(word_count)
    file.close()