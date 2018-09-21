'''
def do_nothing():
    return
print(do_nothing())
def make_result1():
    return 'a','b',1
b= make_result1()
print(b, type(b))

s={오뎅:300,순대:400,만두:500}
menu = input('메뉴:')
def make_price(meun):
    make_dic={'오뎅':300,'순대':400,'만두':500}
print('가격 : {0}'.format(make_dic.get())'''
'''def g(make) :
    make[0]= 0
tt=[1,2,3]
g(tt)
al=[3,3,3]
g(al)
print(tt)
print(al)
def h(t):
    t=(10,20)
b=[1,2,3]
h(b)
a=(4,5,6,7)
h(a)
print(b)
print(a)
def area(width, height):
    print("width:{0}, height:{1}".format(width,height))
area(height=70, width=50)
area(10,20)
def Who_are_you(name,age=5,gender):
    print('이름:{0},나이:{1},성별:{2}'.format(name,age,gender))
Who_are_you('일지매','F')
'''
def reverse(s) :
    return s[::-1]
instr = input('입력>')
print(type(instr))
print('결과>'+reverse(instr))
def sum(**a):
    total=0
    print(a, type(a))
    for i in a:
        total += i
    return total
result = sum(1,2,3,4,5)
print(result)

