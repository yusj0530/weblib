'''
a=dict(one=1, two=2, three=3)
b={'one':1, 'two':2,'three':3}
c=dict(zip(['one','two','three'], [1,2,3]))
d=dict([('two',2),('one',1),('three',3)])
e=dict({'three':3,'one':1,'two':2})
print(a,b,c,d,e)

dic={'name':'홍길동','phone':'010-0000-0000'}
print(dic['name'], type(dic))
dic1={'스포츠':['축구','농구','배구']}
print(dic1['스포츠'],type(dic1))
dic2=['']
'''
'''
dic2={'basketball':5,'soccer':11,'baseball':9}
print(dic2,type(dic2))
dic2['tennis']=2
print((dic2.pop('tennis')))

dic2['soccer']=7
print(dic2)
dic2.update(basketball=7)

del dic2['soccer']
print(dic2)

dic2={('농구','야구'):['농구','야구']}
print(dic2)

dic={'basketball':5,'soccer':11,'baseball':9}
key=dic.keys()
print(key, type(key))
key_list=list(key)
print(key_list, type(key_list))
value=dic.values()
print(value, type(value))
items=dic.items()
print(items, type(items))
items_list=list(items)
print(items_list, type(items_list))
print(len(dic))
print('soccer' in dic)
print('tennis' not in dic)
'''
'''
dic={'basketball':5,'soccer':11,'baseball':9}
items= dic.items()
print(items, type(items))
s1={2,1,3}
print(s1, type(s1))
s2=set([3,2,1])
print(s2, type(s2))
s3=set('321')
print(s3, type(s3))
s4=set(['3','2','1'])
print(s4, type(s4))
l1= list(s4)
print(l1,type(l1))
print(l1[1])
print(s1[1])
'''
'''
ss1=set([1,2,3])
ss2=set([3,4,5,6])
print(ss1 & ss2)
print(ss1.intersection(ss2))
print(ss1 | ss2)
print(ss1.union(ss2))
print(ss1-ss2)
print(ss1.difference(ss2))
print(ss2 - ss1)
print(ss2.difference(ss1))

ss1={1,2,3}
ss1.add(4)
ss1.add(1)
ss1.discard(6)
ss1.remove(4)
ss1.update({100,200})


print(ss1)
'''
'''
s="""We encourage everyone to contribute to Python. If you still have 
questions agter reviewing the material
in this guide, then the Python Mentors group is available to help guide
new contributors through the process."""

s=s.lower().replace('.',' ').replace(',',' ').replace('\n',' ')
s1=s.split()
s2=list(set(s1))
print(s2)
for word in s2:
    print('{0}:{1}'.format(word, s2.count(s2))
'''
seq=range(1,10)
print(seq, type(seq))
print(seq[0:])
print(len(seq))
for i in seq :
    print(i,end= '')
print(list(seq))
seq2=range(1,12,3)
for i in seq2:
    print(i, end='')