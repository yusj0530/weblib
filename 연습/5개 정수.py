
# s=0
# l=[]
# while (len(l)!=5):
#     n=input(">>>")
#     if(n.isdigit()==False):
#         print("숫자를 입력하세요.")
#         continue
#     n.append(int(n))
#     s+=int(n)
# print(sum(l)/len(l))

l=[]
s=0
while (len(l)!=5):
    num=input(">>>")
    if(num.isdigit() == False):
        print("숫자를 입력하세요")
        continue
    l.append(int(num))
    s+=int (num)
print(sum(l)/len(l))

