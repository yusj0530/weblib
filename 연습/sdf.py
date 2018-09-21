def reverse(s):
        l=[]
        aa=""
        for i in s:
            l.append(i)
            l.reverse()
        for b in l:
            aa+=b
        return aa
def re(string):
    bb= string[::-1]



instr = input('입력> ')
print(type(instr))
#print('결과> '+ reverse(instr))
print("결과>>"+re(instr))






