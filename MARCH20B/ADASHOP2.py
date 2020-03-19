t = int(input())
while t>0:
    r,c = list(map(int,input().split()))
    arr = [(1,1),(8,8),(7,7),(6,8),(8,6),(7,7),(6,6),(4,8),(8,4),
(6,6),(5,5),(2,8),(8,2),(5,5),(4,4),(1,7),(7,1),(4,4),(3,3),(1,5),(5,1),
(3,3),(2,2),(1,3),(3,1)]
   

    if r==c==1:
        print(24)
        for x,y in arr[1:]:
            print(x,y)
    elif r==c!=1:
        print(25)
        for x,y in arr:
            print(x,y)
    else:
        k = (r+c)//2
        print(26)
        print(k,k)
        for x,y in arr:
            print(x,y)
    
    
    t = t-1