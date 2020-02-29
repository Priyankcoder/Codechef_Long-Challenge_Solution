# cook your dish here
def zomcav(n,l,z):
    p=[0]*n
    for i in range(1,n+1):
        a=i-l[i-1]-1
        b=i+l[i-1]-1
        if a<0:
            a=0
        p[a]+=1
        if b+1<n:
            p[b+1]-=1
    for i in range(1,n):
        p[i]+=p[i-1]
    p.sort()
    z.sort()
    if p==z:
        print("YES")
    else:
        print("NO")

for i in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    z=list(map(int,input().split()))
    
    zomcav(n,l,z)