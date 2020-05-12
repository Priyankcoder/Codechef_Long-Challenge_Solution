
t = int(input())
while t>0:
    n, m, k = list(map(int,input().split()))
    count = 0
    flag = 0
    ans = []
    for i in range(n):
        arr = list(map(int,input().split()))
        ans.append(arr[count])
        if count <= k-2:
            count += 1
        else:
            count = 0
    print(*ans)

    t = t-1

    
                
            
        
    
    
    
    
    