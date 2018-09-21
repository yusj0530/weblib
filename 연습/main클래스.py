
class MyString(str):
    pass

class ASD(str):
    pass

s= MyString()
print(type(s))
print(MyString.__name__)
d=ASD()
print(type(d))
print(ASD.__name__)

print(type(t))