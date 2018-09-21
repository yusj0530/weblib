a=[1,2,3] ; b=[4,5,a]; c= [a,b,100]
import copy
print("c의 값:",c)
print("c의 주소: " , hex(id(c)))
d= copy.deepcopy(c)
f=copy.copy(c)
print('f의 주소: ', hex(id(f)))
print("d의 주소: ", hex(id(d)))

c[2]=5; c[0][1]=10
print(c)
print('f의 값: ',f)
print("d의 값: ",d)

