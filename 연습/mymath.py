class UserException(Exception):
    def __init__(self, name, age):
        Exception.__init__(self)
        self.name =name
        self.age = age

def checkPerson(name, age):
    try:
        if age>20 :
            print("안녕하세요 {0}님 입장가능 입니다.".format(name))
        else:
            raise UserException(name, age)
    except UserException as ex :
        print("User Exception이 발생했습니다. {0}님 나이가 {1} 이시라 입장 불가입니다.".format(ex.name, ex.age))

checkPerson("홍길동", 21)
checkPerson("일지매", 19)