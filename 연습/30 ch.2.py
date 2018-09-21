'''
aa=[10, 100,1000,10000]
aa.append(100000)
print(aa)
print(aa)
aa=[10,100,1000,10000]
aa.insert(0,2)
print(aa)
aa=[10,100,1000,10000]
aa.remove(100)
print(aa)
aa=[10,100,1000,10000]
print(aa.index(100))
'''
'''
aa=[1,5,3,9,8,4,2]
aa.sort()
print(aa)
aa.sort(reverse=True)
print(aa)
aa=[10,99,22,9,8]
aa.sort(key=str)
print(aa)
aa.sort(key=int)
print(aa)

li[2:5]=[5]
li.sort()
print(li*3)

li.append(5)
li[2:5]=[]
li.sort()
print(li*3)

li=[3,2,'a','b','c',1,6,4,8,7]
li.index('a')
print(li)
'''
stack=[]
stack.append(10)
stack.append(20)
stack.append(30)
print(stack)
print("stack : ", stack.pop())
print("stack : ", stack.pop())
print("stack : ", stack.pop())

queue=[]
queue.append(10)
queue.append(20)
queue.append(30)
print(queue)
print("queue : ", queue.pop(0))
print("queue : ", queue.pop(0))
print("queue : ", queue.pop(0))


