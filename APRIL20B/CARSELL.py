def codechef(n,arr):
    #cook your dish here
    arr.sort(reverse = True)
    profit = 0
    loop = 0
    m = 1000000007
    for i in range(len(arr)):
        profit +=  max(0,arr[i]-loop)
        profit  = profit%m
        loop += 1
    return profit
        
    
    
    

if __name__ == "__main__":
    t = int(input())
    while t>0:
        n = int(input())
        arr = list(map(int,input().split()))
        print(codechef(n,arr))
        t = t-1
    
    
                
            
        
    
    
    
    
    