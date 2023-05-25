#08_python_Day_7
#python7_10
led=[
    ["xxxx",
     "x--x",
     "x--x", #0
     "x--x",
     "xxxx"],
    ["---x",
     "---x",
     "---x", #1
     "---x",
     "---x"],
    ["xxxx",
     "---x",
     "xxxx", #2
     "x---",
     "xxxx"],
    ["xxxx",
     "---x",
     "xxxx", #3
     "---x",
     "xxxx"],
    ["x--x",
     "x--x",
     "xxxx", #4
     "---x",
     "---x"],
    ["xxxx",
     "x---",
     "xxxx", #5
     "---x",
     "xxxx"],
    ["x---",
     "x---",
     "xxxx", #6
     "x--x",
     "xxxx"],
    ["xxxx",
     "---x",
     "---x", #7
     "---x",
     "---x"],
    ["xxxx",
     "x--x",
     "xxxx", #8
     "x--x",
     "xxxx"],
    ["xxxx",
     "x--x",
     "xxxx", #9
     "---x",
     "---x"]
    ]
s=str(input())
for i in range(0,len(led[0])):
    for j in range(0,len(s)):
        a=int(s[j])
        print(led[a][i],"\t",end="")
    print()
