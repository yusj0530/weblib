s={'오뎅':300,'순대':400,'만두':500}
menu = input('메뉴: ')
def make_price2(menu,**items):
     print("{0}는{1}원 입니다.".format(menu,items.get(menu)))

make_price2(menu,오뎅=300,순대=400,만두=500)
