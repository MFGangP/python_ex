# 문제
# 문자열 안에 있는 문자의 개수, 숫자의 개수, 공백의 개수를 계산하는 프로그램을
# 작성하시오.
# 출력결과
# 문자열을 입력하시오 : A picture is worth a thousand words.
# {'digits' : 0, 'spaces' : 6, 'alphas' : 29}
# --------------------------------------------------------------------------
def main():
    count_str = 0
    count_dig = 0
    count_spc = 0
    string = list(input("문자열을 입력하시오 : "))

    for i in range(len(string)):
        for C_S in range(65, 91):       # 알파벳 대문자 검출
            if ord(string[i]) == C_S:
                count_str += 1
        for S_s in range(97, 123):      # 알파벳 소문자 검출
            if ord(string[i]) == S_s:
                count_str += 1

        for d_s in range(48, 58):       # 숫자 검출
            if ord(string[i]) == d_s:
                count_dig += 1

        if ord(string[i]) == 32:        # 공백 검출
            count_spc += 1
    print("'digits' : " ,count_dig, "', spaces' : ",count_spc, ", 'alpha' : ",count_str)

if __name__ == "__main__":
    main()

# def main():
#     string = input("문자열을 입력하세요 : ")
#     dic1 = {"alphas":0, "digits":0, "spaces":0}
#     for i in string:
#         # 알파벳이라면....
#         if i.isalpha():
#             dic1["alphas"] += 1
#         # 숫자라면
#         if i.isdigit():
#             dic1["digits"] += 1
#         # 공백이라면...
#         if i.isspace():
#             dic1["spaces"] += 1
#
#     print(dic1)
#
# if __name__ == "__main__":
#     main()
