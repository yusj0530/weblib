'''def cheak_fun(**a):
    print(a, type(a))
cheak_fun(soccer=11,tennis=2)
def f(a,b,c,*args,**kwd):
    print(a,b,c ,type(a))
    print(args, type(args))
    print(kwd, type(kwd))
f(10,20,30,40,depth=10, width=20)
def clean_strings(strings, *funcs):
    results = []
    for string in strings :
        for func in funcs :
            string= func(string)
            results.append(string)
    return results;
city=['Seoul', 'Bu san','ln chon', 'Deajon']
result = clean_strings(city,str.upper, str.lower)
print(result)
s=
meun= input('메뉴: ')
def (meun, **menu_dict):
    make_dic={'오뎅':300,'순대':400,'만두':500}
print(", 메뉴: {1}".format(make_dic.get))\

def make_price(menu, **menu_dict):
    print('가격 : {0}'.format(menu_dict.get(meun,'없네요')))
make_price2={'오뎅':300,'순대':400,'만두':500}
#함수 s를 만드세요 이 함수는 임의의 개수의 인수를 받아서 그 합을 계산합니다.
def s(*a):
    total=0
    print('a:' , a)
    for i in a :
        total += i
        return  total
print(s())
print(s(1,2))
print(s(1,2,3,4,5,6,7,8,9,10))
def change_value (x, value) :
    x=value
    print("x:{} in change_Value".format(x))
x=5
change_value(x,20)
print("x:{} in change_Value".format(x))
print(globals())
'''
def change_value(s) :
    s= 'abcde'
    print(s)
s='zzzzz'
print(s)