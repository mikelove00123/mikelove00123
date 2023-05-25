w=int(input(""))
h=int(input(""))

bmi=w/(h**2)

if bmi>=30:
    print("อ้วนอันตราย")
elif bmi<=29.9 and bmi>=25:
    print("โรคอ้วน ระดับที่ 1")
elif bmi<=24.9 and bmi>=23:
    print("น้ำหนักเกิน")
elif bmi<=22.9 and bmi>=18.5:
    print("สมส่วน")
else:
    print("ตำกว่าเกณฑ์") 