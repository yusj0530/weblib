def sum(*a):
    total= 0
    print(a,type(a))
    for i in a:
        total +=i
    return total
result = sum(1,2,3,4,5)
print(result)