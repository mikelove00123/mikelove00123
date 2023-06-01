import math
def Taxi(dist=10):
    distance = dist
    #print(distance)
    distance2 = distance-math.floor(distance)
    distance = math.floor(distance)
    box = 0
    check={10:6.5,20:7.5,40:8,60:9,80:10.5}
    for i in range(1,distance+1):
        #print('กิโลเมตรที่: ',i)
        if i == 1:
            tx = 35
        elif  i >1 and i <=10:
            tx = 5.5
        elif  i >10 and i <=20:
            tx = 6.5
        elif  i >20 and i <=40:
            tx = 7.5
        elif  i >40 and i <=60:
            tx = 8
        elif  i >60 and i <=80:
            tx = 9
        else:
            tx = 10.5
        box += tx
    if distance in check:
        tx = check[distance]
        extra = distance2*tx
    else:
        tx = tx
        extra = distance2*tx
    print("TX: ",tx)   
    calculate = round(box+extra)
    print(f'คุณเดินทาง:  {dist} กิโลเมตร\nต้องจ่ายค่าแท๊กซี่: {calculate} บาท')
while True:
    dist = float(input("Enter KM: "))
    Taxi(dist)
    print("-----------------------------") 