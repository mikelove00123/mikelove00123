t=[]
n=int(input(""))
for i in range(0,n):
    t.append((int(input(""))))
s=[]
for i in range(0,n//2):
    s.append(t[i] + t[n-1-i])
print(s)

