'''
s= "spam and ham"
t = s.split()
print(t, type(t))
t=s.split("and")
print(t)

s2=":".join(t)
print(s2, type(s2))
s3="one:two:three:four:five"
t=s3.split(":",3)
'''

'''
lines ='''1st line
2st line
3st line
4st line
'''
'''

'''
print(lines.splitlines(), type(lines))

lines2="1st line \n 2st line \n 3st line \n 4st line "


#질문하기
print('1234'.isdigit())
print('abcd'.isdigit())
print('1234'.isalpha())
print('ABCD'.isupper())
print('abcd')
print('\n\n'.isspace())
print('  '.isspace())
print(''.isspace())

s="i have %d apple"%5
print(s)
s="interest rate is %f" %1.24
print(s)
s="interest rate is %2.4f" %1.24
print(s)

s="I have {%d} apples, and i ate {%d} apples.".format(%5,%3)
print(s)
print('i have',5,'apples, and i ate',3 ,'apples.')
s="I have {total} apples, and I ate {num} apples.".format(total=5,num=3)
print(s)
s="I have {total} apples, and I ate {num} apples.".format_map({"total":5, "num" :3})
print(s)

.lstrip(',')
'''


'''
s='/usr/local/bin/python'
t=s.split("/")
s1=",".join(t)
s2=s1.lstrip(',')
print(s2)
'''
