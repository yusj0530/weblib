def 성모():
    while True:
        s=input(">>>")
        if(s.isdigit()==True):
            break
        if(s.islower()==False):
            print("소문자 pleaseㅠㅠ")
        if(s.islower()==True):
            aa=s[0].upper()+ s[1:].lower()
            print(aa)
성모()