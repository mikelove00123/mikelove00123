class Student():
    name=""
    surname=""
    score=""

student=[]
for i in range(0,3):
    student.append(Student())
    print("plese input name %d :"%(i+1))
    student[i].name=input()
    print("plese input surname %d :"%(i+1))
    student[i].surname=input()
    print("plese input score %d :"%(i+1))
    student[i].score=int(input())

maxx=student[0]
for i in range (0,len(student)):
    if maxx.score < student[i].score:
        maxx=student[i]
print("นักเรียนที่ได้คะแนนสูงที่สุดคือ %s %s %s " %
        (maxx.name,maxx.surname,maxx.score))
       