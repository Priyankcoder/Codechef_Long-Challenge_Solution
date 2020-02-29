def chef(n,arr):
    a=sum(arr)
    av=a/n
    
    for i in arr:
        if av==(a-i)/(n-1):
            print(arr.index(i)+1)
            break
    else:
        print("Impossible")

for i in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    chef(n,arr)