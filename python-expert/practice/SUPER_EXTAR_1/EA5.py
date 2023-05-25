#is not triangle        = ไม่ใช่สามเหลี่ยม
#equilateral triangle   = สามเหลี่ยมด้านเท่า
#isosceles triangle     = สามเหลี่ยมหน้าจั่ว
#scalene triangle       = สามเหลี่ยมด้านไม่เท่า
#right triangle         = สามเหลี่ยมมุมฉาก
#obtuse triangle        = สามเหลี่ยมมุมป้าน
#acute-angled triangle  = สามเหลี่ยมมุมแหลม

#4,4,3 output = acute-angled triangle, isosceles triangle
#5,9,7 output = obtuse triangle, scalene triangle
#5,6,1 output = is not triangle

import sys
a = int(input())
b = int(input())
c = int(input())

if a>=b and a>=c:
    x=a
    y=b
    z=c
elif b>=a and b>=c:
    x=b
    y=a
    z=c
else:
    x=c
    y=b
    z=a

if x >= y+z:
    print("is not triangle")
    sys.exit(0)
if x**2 == y**2+z**2:
    print("right triangle")
elif x**2 > y**2+z**2:
    print("obtuse triangle")
else:
    print("acute-angled triangle")

if a==b and b==c:
    print("equilateral triangle")     
elif a==b or b==c or a==c:
    print("isosceles triangle")
else:
    print("scalene triangle")
