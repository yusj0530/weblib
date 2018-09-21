ss= input("입력>>")
if ss.isdigit()==False:
    print("숫자를 입력하세요.")
else :
    ss=int(ss)
    if ss % 3==0:
        print("이 숫자는 3의 배수입니다.")
    else:
        print("이 숫자는 3의 배수가 아닙니다.")