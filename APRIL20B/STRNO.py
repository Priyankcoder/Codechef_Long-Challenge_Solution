from math import sqrt
from math import sqrt
def prime(p):
    total = 0
    for i in range(2, int(sqrt(p))+1):
        count = 0
        if p%i == 0:
            while p > 1 and p%i == 0:
                count += 1
                p = p//i
            #print(count)
            total += count
    if p>1: 
        total += 1
    return total
    
        
def codechef(x,k):
    dx = prime(x)
    p = 2<<(k-1)
    if x >=p and k <= dx:
        return 1
    else:
        return 0
    
    

if __name__ == "__main__":
    t = int(input())
    while t>0:
        
        x, k = list(map(int,input().split()))
        print(codechef(x, k))
        t = t-1
    
    
                
            
        
    
    
    
    
    