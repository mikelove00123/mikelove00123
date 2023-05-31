'''
0-1 km  = 35
2-10 km = 5.5
11-20 km = 6.5
21-40 km = 7.5
41-60 km = 8
61-80 km = 9
81 km^ = 10.5
'''
import math

distance = float(input("จำนวนที่วิ่ง: ")) #km
#print(distance)
distance2 = distance-math.floor(distance)
distance = math.floor(distance)

box = 0
for i in range(1,distance+1):
    #print('กิโลเมตรที่: ',i)
    if i == 1:
        tx = 35
    elif  i >=2 and i <=10:
        tx = 5.5
    elif  i >=11 and i <=20:
        tx = 6.5
    elif  i >=21 and i <=40:
        tx = 7.5
    elif  i >=41 and i <=60:
        tx = 8
    elif  i >=61 and i <=80:
        tx = 9
    else:
        tx = 10.5
    box += tx

calculate = round(box + distance2 * tx)

print("ราคาที่ต้องจ่าย: ",calculate)