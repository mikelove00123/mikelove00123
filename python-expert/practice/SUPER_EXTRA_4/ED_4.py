#08_python_Day_7
#python7_5
def large(a,b):
    return a if a>b else b
    return a if a>b else b
a=int(input())
b=int(input())
c=int(input())

def large3(a,b,c):
    m=a
    m=large(m, b)
    m=large(m, c)
    return m
print(large3(a,b,c))