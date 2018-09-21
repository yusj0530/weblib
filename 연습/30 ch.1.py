'''
aa=[10, 100, 1000]
print(aa, type(aa))
ab=(10, 100, 1000, 'Python', 'Java')
print(ab, type(ab))

aa=[10, 100, 1000, 10000]
print(aa[0])
print(aa[-1])
ac= [10, 100, 1000, ['천', '만']]
print(ac)
print(ac[-1], type(ac))
print(ac[:2])
print(ac[-2:])
print(ac[1:3])
'''
'''
al =[1,2,3,4,]
bl=[5,6,7,8]
cl=al+bl
print(cl)
#str 말고 int로 하려면?
print("al Lenght : "+str(al.__len__()))
print("bl Lenght : "+str(cl.__len__()))
#len() 함수
al=[1,2,3,4]
dl= al*3
print(dl)
print("dl Lenght : "+str(dl.__len__()))
'''
'''
al=[1,2,'3',4]
al[1]='둘'
print(al)
al[2]=al[2]+'3'
print(al)
al=[1,2,3,4]
al[1]='둘', '셋','넷'
print(al)
al=[1,2,3,4]
al[1:3]=['둘', '셋', '넷']
print(al)
al=[1,2,3,4]
al[1]=['둘','셋','넷']
print(al)
del al[1:3]
print(al)
al=[1,2,3,4]
del al[1]
print(al)
al=[1,2,3,4]
del al[1:3]
print(al)
'''