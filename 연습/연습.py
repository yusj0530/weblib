'''
al=[1,2,3,4]
bl=[5,6,7,8]
cl=al + bl
print(cl)

#메뉴 : 오뎅:300,순대:400,만두:500,라면:
총합



menu = input('메뉴:')
if menu == '오뎅' menu == '순대'
    print(300)
elif:
    print(400)
elif menu == '만두':
    print(500)
elif menu == '라면':
else: '메뉴에 없습니다.'
'''
'''
#menu = input('메뉴:')
s={'오뎅':300,'순대':400,'만두':500,'라면':1000}
key=input('메뉴:')
key=key.split()
sum=0
for a in key :
    price=s.get(a,-1)
    if price==-1 :
        print("그런 메뉴는 없습니다.")
    else :
        print('메뉴 {0}은 {1}원 입니다.'.format(a,price))
        sum += price
else:
    print(sum)
#print('메뉴 {1} 가격:{0}'.format(menu_dict.get(menu, '그런 메뉴는 없네요').menu))


al=[1,2,3,4,]
bl=[5,6,7,8]
cl=al+bl
print("al Lenght : "+ str(al.__len__()))
print("cl Lenght : "+ str(cl.__len__()))
al[1]='둘'
al[2]=al[2]+3
print(al)
al[1]= ['둘','셋', '넷']
print(al,type(al[1]))
print(al.index(1))
al=[3,6,1,8,5,9,3]
al.sort()
print(al)
al=['가','마','다','나']
al.sort()
print(al)
'''
tu1=()
print(tu1,type(tu1))
tu2=(1,2,3,('a','b'))
A,B,C,D=tu2
print(A,B,C,D,type(A))
print(tu2[1], type(tu2))