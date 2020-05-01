from math import sqrt
def SieveOfEratosthenes(n): 
      
    # Create a boolean array "prime[0..n]" and initialize 
    #  all entries it as true. A value in prime[i] will 
    # finally be false if i is Not a prime, else true. 
    prime = [True for i in range(n+1)] 
    p = 2
    while (p * p <= n): 
          
        # If prime[p] is not changed, then it is a prime 
        if (prime[p] == True): 
              
            # Update all multiples of p 
            for i in range(p * p, n+1, p): 
                prime[i] = False
        p += 1
      
    # Print all prime numbers 
    return prime
if __name__ == "__main__":
    t = int(input())
    while t>0:
        n = int(input())
        if n == 1:
            print(1)
        else:
            print(n//2)
        
        if n<4:
            a_p = [i for i in range(1, n+1)]
            print(n, end = " ")
            print(*a_p)
        else:
            r = int(sqrt(n))
            p_arr = SieveOfEratosthenes(n)
            rp = []
            for p in range(2, n+1): 
                if p_arr[p]:
                    rp.append(p)
            
            print(len(rp)+1, end = " ")
            print(1, end = " ")
            print(*rp)
            p_arr = [True]*(n+1)
            for i in rp:
                p_arr[i] = False
            p_arr[1] = False
            lo = 4        # Run the loop until getting 2's power smaller than n
            pwr = 2       # increase the power
            
            while lo<= n:
                page = []
                p_c = 0
                
                for ele in rp:
                    if ele>r:
                        break
                    v = ele**pwr
                    if v <= n :
                        p_arr[v] = False
                        page.append(v)
                        p_c += 1
                pwr+=1
                lo = lo<<1
                print(p_c, end = " ")
                print(*page)
            for i in range(1,n+1):
                if p_arr[i] == True:
                    if i+1 <= n and p_arr[i+1] == True:
                        print("{} {} {}".format(2,i,i+1))
                        p_arr[i+1] = False
                    else:
                        print("{} {}".format(1,i))
                    p_arr[i] = False
                
        t = t-1
    
    
                
            
        
    
    
    
    
    