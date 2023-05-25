#โปรแกรมแปลงอุณภูมิ
'''temp=input("")
degree=int(temp[:-1])
unit=temp[-1].upper()


if unit=="C":
    result=(9*degree)/5+32
    unit_result="ฟาเรนไฮ"
if unit=="F":
    result=(degree-32)*5/9
    unit_result="เซลเซียส"
print("แปลงตัวเลข = ",temp," เป็น ",unit_result," = ",result)
'''

#loop while
'''i=1

while i<=3:
    print("hello")
    i=i+1
print("end")'''

#โปรแกรมบวกตัวเลข

i=1
sum=0
avg=0
while i<=5:
    sum+=i
    print("รอบที่ = ",i,"รวมครั้งที่ : ",sum)
    i+=1
print("ผลรวมทั้งหมด : ",sum)
