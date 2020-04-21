def codechef(n,arr):
    flag = 1
    #cook your dish here
    for i in range(len(arr)):
        if arr[i] == 1 and i < len(arr)-1:
            for j in range(i+1,min(i+6, len(arr))):
                if arr[j] == 0:
                    continue
                else:
                    return "NO"
    return "YES"
    
    
                    
if __name__ == "__main__":
    t = int(input())
    while t>0:
        n = int(input())
        arr = list(map(int,input().split()))
        print(codechef(n,arr))
        t = t-1
    
    
                
            
        
    
    
    
    
    