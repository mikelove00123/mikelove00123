#08_python_Day_7
#python7_8
board=[['a','b','c','d'],
        ['e','f','g','h'],
        ['i','j','k','l'],
        ['m','n','o','p']]
def printboard(bb):
    for x in bb:
        for y in x:
            print(y,end="")
        print()
while True:
    printboard(board)
    k=int(input())
    if k == -1:
        break
    l=input("")
    if l == 'l':
        temp = board[k][0]
        del board[k][0]
        board[k].append(temp)
    elif l == 'r':
        temp=board[k][3]
        del board[k][3]
        board[k].insert(0,temp)
    elif l == 'u':
        temp = board[0][k]
        for i in range(0,3):
            board[i][k]=board[i+1][k]
        board[3][k]=temp
    elif l == 'd':
        temp = board[3][k]
        for i in range(0,3):
            board[i][k]=board[i][k]
        board[0][k]=temp