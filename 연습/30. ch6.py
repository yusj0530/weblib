#메뉴 : 오뎅:300,순대:400,만두:500

'''
menu = input('메뉴:')
if menu == '오뎅':
    print(300)
elif menu == '순대' :
    print(400)
elif menu == '만두':
    print(500)
else: '메뉴에 없습니다.'

menu=key
menu = input('메뉴:')
menu_dict={'오뎅':300,'순대':400,'만두':500}
print('메뉴 {1} 가격:{0}'.format(menu_dict.get(menu, '없네요').menu))
print('메뉴 {1} 가격:{0}'.format(menu_dict[menu].menu))

'''
'''
list1=['a','b','c']
for i in list1:

    if i == 'b' :
        break
    print(i)
else :
    print("for문 작업 완료")

list2=[(1,2),(3,4),(5,6)]
for (first, last) in list2 :
    print('first :', first, 'last:', last)
'''
'''
colors =['red','orange','blue','black']
for index,color in enumerate(colors) :
    print('index :', index, 'colors :', color)

list1=[1,3,5,7,9,10,11,13]
for x in list1:
    if x %2 == 0 :
        break
        print(x)

list1 = ['a','b','c']
for x in list1 :
    if(x == 'b') :
        continue
    print(x)

list1 = [1,2,3,4,5,6,7,8,9]
result = []
for i in list1 :
    result.append(i *2)
print(result, end=" ")

result1 = [i*2 for i in list1]
print(result1, end=" ")
result2 = [i*2 for i in list1 if i %2 == 0 ]
print(result2)
'''
'''
i = [10,12,14,15,17,18,19,20,25,30,32,33,37,40,42,44,46,50]
count=0
sum = 0
for n in i :
    if n % 3 == 0 :
        count += 1
        sum +=n
print("주어진 리스트에서 3의 배수의 개수 ==>{0}
주어진 리스트에서 3의 배수의 합 ==>{1}".format(count, sum))

for n in range(1, 100):
    s = str(n)
    c = s.count('3')+s.count('6')+s.count('9')
    if c < 1:
        continue
    print("{0} {1}".format(s, '짝'*c))

list=[(1,2),(3,4)]
print(list[0][1])

for n in range(1, 100) :
    s=str(n)
    c = s. count('3')+s.count('6')+s.count('9')
    if c<1:
        continue
    print("{0} {1}".format(s,'짝'*c))
    '''