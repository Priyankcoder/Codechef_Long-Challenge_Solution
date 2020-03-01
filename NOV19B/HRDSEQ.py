t = int(input())
while t>0:
    n = int(input())
    a = [0,0]
    total = 0
    d = n
    while d-2 > 0:
        if a[0] in a[1:]:
            a.insert(0,(a[1:].index(a[0]))+1)
        else:
            a.insert(0,0)
        d = d-1
    if n == 1:
        print(1)
    
    elif n == 2:
        print(2)
    
    else:
        b = a[0]
        for j in a:
            if j == b:
                total+=1
        print(total)
    t = t-1
    