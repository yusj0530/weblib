'''x=20
x=20
def scope_test():
    x=100
    print('함수내 변수 x 값 :',x , id(x))

scope_test()
print('전역 변수 x 값:', x, id(x))
def scope_test1():
    global x
    x= 100
    print("함수내 변수 x 값:", x, id(x))
scope_test1()
print('전역 변수 x 값:', x, id(x))
for i in range(10) :
    print("{0}:{1}".format(i,(lambda x : x **2 )(i)), end=" ")
else:
    print()
'''
number= input("입력:")
if number.isdigit() == False:
    print("숫자입력")
number= int(number)
if number %3 == 0 :
    print("3의 배수")
else:
    print("3의 배수가 아니다.")