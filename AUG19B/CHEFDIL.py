def cardgame(s):
    x=0
    y=0
    for i in s:
        if i=='0':
            x+=1
    
        else:
            y+=1
    if (y==1 and x==1) or (y%2!=0 and x%2==0) or (y%2!=0 and x%2!=0):
        print("WIN")
    else:
        print("LOSE")
for i in range(int(input())):
    s=str(input())
    cardgame(s)