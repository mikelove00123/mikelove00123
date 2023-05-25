W = float(input("weight(kg): "))
H = float(input("Height(m): "))
H = H/100
BMI = W/(H**2)
if BMI <20:
    print("Thin")
else:
    if BMI >25:
        print ("Fat")
    else:
        print ("Normal")        