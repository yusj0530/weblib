'''f=open('d:\\새\\file_test.txt', 'w')
f.write("Hello Python")
f.close()

f=open('c:\\Users\bit34\Python\\file_test.txt','w')
f.write("Hello Python")
f.close()
f=open('d:\\새\\file_test.txt', 'w')
for i in range(5):
    ss="%d번쨰 줄을 작성 했습니다,\n"%i
    f.write(ss)
f.close()


f=open('d:\\새\\file_test.txt', 'r')
datas =f.readlines()
print(type(datas))
for data in datas:
    print(data,(','.join(data.split())))
f.close()

f=open('d:\\새\\file_test.txt', 'r')
data=f.read()
print(data, type(data))
f.close()


f_src=open('d:\\새\\puppy.jpg', 'rb')
data= f_src.read()
f_src.close()

f_dest= open('d:\\새 폴더\\puppy1.jpg','wb')
f_dest.write(data)
f_dest.close()

with open('d:\\새\\file_test.txt', 'r') as f :
    for line in f.readlines() :
        print(line, end= "\n")
print("파일이 close 되었나 : ", f.closed)
'''

f=open('d:\\새\\file_test.txt','r')
f_dest=open('d:\\새\\file_test_copy.txt','w')
while True:
    data=f.readlines()
    f_dest.write(data)
    if not data : break

