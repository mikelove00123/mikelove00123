x=[]
for i in range(0,10):
    n = int(input(""))
    x.append(n)

count=0
#i=0

#แบบที่ 1 
'''while i < len(x):
    if x[i]%2==0:
        count=count+1
    i+=1
print(count)'''

#แบบที่ 2
'''for i in range(0,len(x)):
    if x[i]%2==0:
        count=count+1
print(count)'''

#แบบที่ 3
for y in x:
    if y%2==0:
        count=count+1
print(count)