a = 1
while a<1000:
    if a%3==0 and a%5==0 and a%7==0:
        pass
    elif a%3==0 and a%5==0:
        print(a)
    elif a%5==0 and a%7==0:
        print(a)
    elif a%3==0 and a%7==0:
        print(a)
    a=a+1
