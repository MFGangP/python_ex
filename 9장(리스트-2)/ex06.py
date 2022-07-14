# 연락처 관리 프로그램 만들기
# 출력결과
# ------------------------
# 1. 친구 리스트 출력
# 2. 친구추가
# 3. 친구삭제
# 4. 이름변경
# 9. 종료
# 메뉴를 선택하시오: 2
# 이름을 입력하시오: 홍길동
# ------------------------
# 1. 친구 리스트 출력
# 2. 친구추가
# 3. 친구삭제
# 4. 이름변경
# 9. 종료
# 메뉴를 선택하시오: 1
# ['홍길동']
# ------------------------

# 출력 문구를 나타내는 함수
def menu_print():
    print("1. 친구 리스트 출력")
    print("2. 친구추가")
    print("3. 친구삭제")
    print("4. 이름변경")
    print("9. 종료")

name_list = []  # 친구 목록을 저장할 리스트
phone_list = []
while True:
    # print("1. 친구 리스트 출력")
    # print("2. 친구추가")
    # print("3. 친구삭제")
    # print("4. 이름변경")
    # print("9. 종료")
    menu_print()
    menu = int(input("메뉴를 선택하시오 : "))    # 메뉴 번호를 저장
    if menu == 1:
        print(name_list)
        print(phone_list)
        print("-------------------------------")
    elif menu == 2:     # 친구 추가
        name_list.append(input("이름을 입력하시오 : "))
        phone_list.append(input("번호를 입력하시오 : "))
        print(name_list)
        print(phone_list)
        print("-------------------------------")
    elif menu == 3:     # 친구 삭제
        del_name = input("삭제 할 이름을 선택하세요 : ")
        if del_name in name_list:
            del_num = name_list.index(del_name)
            name_list.remove(del_name)
            print(del_name,"님이 삭제되었습니다.")
        else:
            print(del_name,"님이 존재하지 않습니다..")
        print(name_list)
        print(phone_list)
        print("-------------------------------")
        # name_list.remove(input("삭제할 친구를 입력하시오 : "))
        # print(name_list)
    elif menu == 4:     # 친구 이름 변경
        index_name = input("변경 할 이름을 선택하세요 : ")
        if index_name in name_list:
            index = name_list.index(index_name)
            name_list[index] = input("변경 할 이름을 입력하세요 : ")
            phone_list[index] = input("변경 할 번호를 입력하세요 : ")
        else:
            print(index_name,"님이 존재하지 않습니다.")
        print(name_list)
        print("-------------------------------")
    # 무한 루프 빠져나가는 코드
    elif menu == 9:
        print("프로그램을 종료합니다.")
        break
    else:
        print("등록되지 않은 번호입니다.")
        print("-------------------------------")

# 친구 추가시 연락처도 함께 추가하는 프로그램으로 업데이트 해보기


