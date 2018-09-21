'''
tu1=()
print(tu1, type(tu1))
tu2=(1,)
print(tu2, type(tu2))
t=(1)
print(t, type(t))
tu3=(1,2,3)
print(tu3, type(tu3))
tu4=1,2,3
print(tu4, type(tu4))
tu5=('a','b','c',(1,2))
print(tu5, type(tu5))
'''
'''
tu1=(1,2,3,4)
print(tu1[0])
print(tu1[1:3])
tu1=(1,2,3)
tu2=

tu1=10,20,30,'Python'
print(tu1, type(tu1))
a,b,c,d=tu1
print(a,b,c,d)
a,b,c,d=[10,20,30,'Python']
print(a,b,c,d)
'''
'''
tu2=(1,2,3,4,5,6)
a, *b=tu2
print(a,b)
*a, b=tu2
print(a,b)
a,b,*c=tu2
print(a,b,c)
a,*b,c=tu2
print(a,type(a))
print(b, type(b))
print(c, type(c))
'''
ti=3,2,'a','b','c',1,6,4,8,7
li=list(ti)
li[2:5]=[5]
li.sort()
tu1=tuple(li*3)
print(tu1)
id1=ti.index('a')
id2=ti.index('c')
ti2=ti[:id1]
ti3=ti[id2+1:]
temp=ti2+(5,)
ti4=temp+ti3
li=list(ti4)
li.sort()
tu2=tuple(li*3)
print(tu2)