from sys import stdin, stdout
def parity(x): 
    y = x ^ (x >> 1); 
    y = y ^ (y >> 2); 
    y = y ^ (y >> 4); 
    y = y ^ (y >> 8); 
    y = y ^ (y >> 16); 
    if (y & 1): 
        return 1
    return 0
if __name__ == "__main__":
    t = int(input())
    res = ""
    for i in range(1,(10**4)+1):
        res += str(parity(i))
    while t>0:
        n, q = [int(c) for c in input().split()]
        arr = [int(c) for c in input().split()]
        odd = 0
        even = 0
        for i in arr:
            if i<=10**4:
               
                if int(res[i-1]):
                    odd += 1
                else:
                    even += 1
                    
            else:
                if parity(i):
                    odd += 1
                else:
                    even += 1
                
        #print(res[0:9])        
        for _ in range(q):
            Q = int(stdin.readline())
            #print(res[Q-1])
            if Q<=10**4:
                if int(res[Q-1]):
                    print(odd,even)
                else:
                    print(even,odd)
            else:
                if parity(Q):
                    print(odd,even)
                else:
                    print(even,odd)
                
        t = t-1
    
    
                
            
        
    
    # arr.remove(suma)
    # arr.remove(suma)
    
    
    
    