x=[]
for i in range(0,10):
    x.append(int(input()))
v=int(input())
have=False
have = v in x
print("V is in array" if have else "is not in array")
#print(v,"is in"if v in x else "is not","in x")