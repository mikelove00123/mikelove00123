#python4_11
'''import sys
sys.stdout.write("*|\t")
i=1
while i<=9:
    sys.stdout.write(str(i)+"\t")
    i+=1
print()
i=1
while i <=77:
    sys.stdout.write("-")
    i+=1
print() #บรรทัดที่ 1,2
j=1
while j<=9:
    sys.stdout.write(str(j)+"|\t")
    i=1
    while i <=9:
        sys.stdout.write(str())
        i+=1
    i=1
    while i<=9:
        sys.stdout.write(str(i*j)+"\t")
        i+=1
    print()    
    j+=1   
'''

import sys
sys.stdout.write("*|")
i=1
while i<=9:
    sys.stdout.write("\t"+str(i))
    i+=1
print()
i=1
while i<=77:
    sys.stdout.write("-" )
    i+=1
print()
i=1
while i<=9:
    sys.stdout.write(str(i)+"|")
    j=1
    while j<=9:
        sys.stdout.write("\t"+str(i*j))
        j+=1
    print()
    i+=1