'''
counter = 1
while counter < 11 :
    print(counter, end=" ")
    counter += 1
else :
    print("*")

sum, i = 0 ,1
while i <= 100 :
    sum += i
    i += 1
print(sum)

i = 0
while i < 100:
    i +=1
    if i < 5 :
        continue
    print(i, end = ' ')
    if i > 10 :
        break
else :
    print('while else block')

while True:
    print('꺼주세요...!!')
'''
'''
l = [10,12,14,15,17,18,19,20,25,30,32,33,37,40,42,44,46,50]
count, sum = 0, 0
size = len(l)
i = 0
while i < size :
    n =l[i]
    if i %3 == 0 :
        count += 1
        sum += i
    i+= 1
print('3배수 개수{0} \n 3배수의 합 {1}'.format(count,sum))

l = [10,12,14,15,17,18,19,20,25,30,32,33,37,40,42,44,46,50]
size = len(l)
count, sum, i = 0
while i < size :
    n = l[i]
'''
#키보드에서 5개의 정수를 입력 받고 /평균을 구하는 프로그램을 작성하시오
l=[]
s = 0
while len(l) != 5 :
    n = input('>>>')
    if n.isdigit() is False :
        print("Error is not digit")
        continue
    l.append(int(n))
    s += int(n)
print(s/len(l))

#print(sum(l)/len(l))